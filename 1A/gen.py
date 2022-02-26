import sys, math

sent = sys.argv[1:]
f = open("F.txt", "w")
i = 1
f.write('{} {} <s>\n'.format(i-1,i))
for k in sent:
    i = i+1
    if k=='XXX':
        print(i-1)
        t = open("words.txt","r")
        vocab = t.read().splitlines()
        #num = math.log(len(vocab)-5)
        num=0
        t.close()
        for m in vocab[1:-4]:
            f.write('{} {} {} {}\n'.format(i-1,i, m.split()[0], num) )
    else:
        f.write('{} {} {}\n'.format(i-1,i,k))
f.write('{} {} </s>\n'.format(i, i+1))
f.write('{}\n'.format(i+1))
f.close()
