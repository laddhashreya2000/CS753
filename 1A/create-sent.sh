#!/bin/bash

python gen2.py $1 $2 $3 $4
fstcompile --acceptor=true --isymbols=words.txt --osymbols=words.txt F.txt | fstarcsort --sort_type=ilabel > F.fst
fstcompose F.fst L.fst | fstshortestpath | fsttopsort | fstproject --project_output | fstrmepsilon | fstprint --isymbols=words.txt --osymbols=words.txt > out.txt
python out2.py
