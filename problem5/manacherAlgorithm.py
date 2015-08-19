__author__ = 'hongtao'

s = "b"
tempStr = "$"
for i in range(0, len(s)):
    tempStr += "#" + s[i]
tempStr += "#&"

#print tempStr

c = 1
r = 1
p = {}
for i in range(1, len(tempStr)-1):
    if r-i <= 0:
        p[i] = 1
    else:
        p[i] = min(p[2*c-i], r-i)
    while ( tempStr[i+p[i]] == tempStr[i-p[i]] ):
        p[i] += 1
    if i+p[i] > r:
        c = i
        r = i+p[i]

max = 0
for i in range(1, len(tempStr)-1):
    if max < p[i]:
        max = p[i]
        ans = i
print tempStr[ans-p[ans]+1: ans+p[ans]]