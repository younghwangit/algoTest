T = int(input())

for i in range(T):
    r,str = input().split()
    r = int(r)
    str_l=[]
    for j in str:
        str_l.append(j*r)
    str_r = ''.join(str_l)
    print(str_r)