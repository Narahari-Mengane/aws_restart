import re

f = open("preproinsulin-seq.txt").read()
op = re.sub('[^a-z]','',f)
open("preproinsulin-seq-clean.txt", "x").write(op)

f1 = open("preproinsulin-seq-clean.txt").read()

op1 = f1[0:24]
open("lsinsulin-seq-clean.txt", "x").write(op1)

op2 = f1[24:54]
open("binsulin-seq-clean.txt", "x").write(op2)

op3 = f1[54:89]
open("cinsulin-seq-clean.txt", "x").write(op3)

op4 = f1[89:110]
open("ainsulin-seq-clean.txt", "x").write(op4)