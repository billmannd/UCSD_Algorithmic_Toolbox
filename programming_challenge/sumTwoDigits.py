#python2
t = ""
s = 0
while s != 2:
    t = raw_input()
    s = len(t.split(' '))
    print sum([int(i) for i in t.split(' ')])



