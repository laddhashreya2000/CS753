#!/bin/bash

sent=$@
trk=`python gen.py $sent`
fstcompile --acceptor=true --isymbols=words.txt --osymbols=words.txt F.txt | fstarcsort --sort_type=ilabel > F.fst
fstcompose F.fst L.fst | fstshortestpath | fsttopsort | fstproject --project_output | fstrmepsilon | fstprint --isymbols=words.txt --osymbols=words.txt > out.txt
python out.py $trk $sent

