"""Reproduce the published EqualFour selection from text-free numeric scores."""
import argparse
import csv
import gzip
import hashlib
import itertools
import json
import math
from collections import Counter
from pathlib import Path

SIGNALS = ('qe', 'cosine', 'qwen', 'margin')
PRIORITY = ('P1', 'T1', 'T2', 'T3_full508', 'F1', 'F2', 'N1')


def rank_twice(values):
    """Twice the zero-based average rank, and its percentile denominator."""
    if len(values) == 1:
        return [1], 2
    return [2*sum(other < value for other in values)
            + sum(other == value for other in values)-1 for value in values], 2*(len(values)-1)


def choose(rows):
    n = len(rows)
    assert n and len({r['candidate_id'] for r in rows}) == n
    assert all(int(r['n_unique']) == n for r in rows)
    assert len({r['training_included'] for r in rows}) == 1
    origins = [g for r in rows for g in r['origins'].split('|')]
    assert sorted(origins) == sorted(PRIORITY), 'Every route must occur in exactly one deduplicated candidate.'
    for r in rows:
        assert r['primary_origin'] == min(r['origins'].split('|'), key=PRIORITY.index)
    sums = [0]*n
    for signal in SIGNALS:
        values = [float(r[f'{signal}_raw']) for r in rows]
        assert all(math.isfinite(v) for v in values)
        numerators, denominator = rank_twice(values)
        for i, r in enumerate(rows):
            expected = numerators[i]/denominator
            assert math.isclose(float(r[f'{signal}_relative_rank']), expected, abs_tol=1e-12, rel_tol=0)
            sums[i] += numerators[i]
    for i,r in enumerate(rows):
        assert int(r['rank_sum_twice']) == sums[i]
        assert int(r['rank_denominator_twice']) == denominator
        assert math.isclose(float(r['weighted_score']), sums[i]/(4*denominator), abs_tol=1e-12, rel_tol=0)
    order = sorted(range(n), key=lambda i:(-sums[i],-float(rows[i]['qe_raw']),PRIORITY.index(rows[i]['primary_origin'])))
    assert sum(int(r['selected']) for r in rows) == 1
    for position,i in enumerate(order,1):
        assert int(rows[i]['selection_position']) == position
        assert int(rows[i]['selected']) == int(position==1)
    winner=rows[order[0]]
    return winner, sum(s==sums[order[0]] for s in sums)>1


def self_test():
    assert rank_twice([1,1,3]) == ([1,1,4],4)
    assert rank_twice([7]) == ([1],2)
    assert rank_twice([3,2,1]) == ([4,2,0],4)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scores',type=Path,default=Path(__file__).with_name('candidate_scores.csv.gz'))
    parser.add_argument('--output',type=Path,help='Optional destination for reconstructed winner IDs; must not exist.')
    args=parser.parse_args()
    self_test()
    counts=Counter(); routes=Counter(); seen=set(); output_rows=[]
    with gzip.open(args.scores,'rt',encoding='utf-8',newline='') as handle:
        for source_id, group in itertools.groupby(csv.DictReader(handle),key=lambda r:r['source_id']):
            assert source_id not in seen, 'Source groups must be contiguous and unique.'
            seen.add(source_id)
            rows=list(group)
            assert all(r['training_included'] in ('0','1') for r in rows)
            winner,tied=choose(rows)
            counts.update(source_pools=1,unique_candidates=len(rows),top_composite_ties=int(tied))
            included=int(winner['training_included'])
            counts['training_sources']+=included
            if included: routes[winner['primary_origin']]+=1
            output_rows.append([source_id,winner['candidate_id'],winner['primary_origin'],winner['weighted_score'],included])
    expected=json.loads(Path(__file__).with_name('verification_summary.json').read_text(encoding='utf-8'))
    assert dict(counts)==expected['counts']
    assert dict(routes)==expected['training_primary_origin_counts']
    digest=hashlib.sha256(args.scores.read_bytes()).hexdigest()
    assert digest==expected['candidate_scores_sha256'], 'Score file checksum differs from the frozen release.'
    if args.output:
        with args.output.open('x',encoding='utf-8',newline='') as handle:
            writer=csv.writer(handle)
            writer.writerow(['source_id','candidate_id','primary_origin','weighted_score','training_included'])
            writer.writerows(output_rows)
    print(json.dumps({'status':'PASSED','counts':dict(counts),'training_primary_origin_counts':dict(routes),'score_file_sha256':digest},indent=2))


if __name__=='__main__':
    main()
