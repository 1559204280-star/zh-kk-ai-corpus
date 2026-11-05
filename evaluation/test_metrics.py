"""Small offline checks; synthetic strings are not corpus samples."""
from evaluate_metrics import compute_metrics

reference=["Бұл алгоритм деректерді өңдейді.","Нейрондық желі үш қабаттан тұрады.","Сандық деректер компьютерде сақталады."]
exact=compute_metrics(reference,reference)
assert abs(exact["bleu"]-100)<1e-8 and abs(exact["chrf_plus_plus"]-100)<1e-8
changed=compute_metrics(["Алгоритм басқа нәтиже береді.",*reference[1:]],reference)
assert changed["bleu"]<100 and changed["chrf_plus_plus"]<100
try:
    compute_metrics(reference,reference[:1])
except ValueError:
    pass
else:
    raise AssertionError("Mismatched input lengths were silently accepted")
print("PASS: exact matches, changed content, and mismatched line counts")
