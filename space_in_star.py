lst = ' asd e13e1 1e12e   2e12e 1  e 21e1    '
lst = lst.split(' ')

string = ''
for i in range(len(lst)):
    if not lst[i]:
        continue
    if lst[i]:
        lst[i] += '*'
        string += lst[i]
string = string[:-1]
print(string)
