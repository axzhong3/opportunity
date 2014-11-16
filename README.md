Usage
------
python -g GOLDEN_FILE -i INPUT_VECTOR_FILE -c COLUMN_NUMBER [-d]

NOTE: COLUMN_NUMBER = 1-7, 1 meaning the last column
NOTE: -d will turn on debug mode to print out precision and recall for each class

e.g.
$ python fmeasure.py -g S1-ADL1.dat -i debug.txt -c 1 -d
class 0: tp = 46271, fp = 0, fn = 1, precision = 1.000000, recall = 0.999978
class 407521: tp = 1153, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 405506: tp = 57, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 408512: tp = 197, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 404516: tp = 271, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 404517: tp = 405, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 404519: tp = 152, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 404520: tp = 244, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 406505: tp = 99, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 406508: tp = 197, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 406511: tp = 200, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 406516: tp = 452, fp = 1, fn = 0, precision = 0.997792, recall = 1.000000
class 406517: tp = 329, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 406519: tp = 149, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 406520: tp = 384, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 404505: tp = 107, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 404508: tp = 249, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
class 404511: tp = 199, fp = 0, fn = 0, precision = 1.000000, recall = 1.000000
F1 = 0.999980