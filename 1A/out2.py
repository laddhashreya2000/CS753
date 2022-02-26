
f = open('out.txt','r')
ans = f.read().splitlines()
sent = [i.split()[3] for i in ans]
print(' '.join(sent[1:-1]))
