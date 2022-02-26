import sys

num = int( sys.argv[1])
sent = sys.argv[2:]
f = open('out.txt','r')
ans = f.read().splitlines()[num].split()
f.close()
sent = ' '.join(sent)
print(sent.replace("XXX", ans[3]))
