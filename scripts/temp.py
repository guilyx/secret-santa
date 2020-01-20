l = [str(i) for i in range(7)]
newstr = ''
for elem in l:
    newstr += elem + ' '
newstr = newstr[:-1]
newlist = [newstr]
print(newstr)
print(newlist)