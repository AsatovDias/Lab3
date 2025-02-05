a = int(input())
pr = 1
for i in range(1,a+1):
    pr*=i
print(pr)
#---------------------
sum_e = 0
sum_o = 0
for j in range(1,101):  
    if j%2 == 0:
        sum_e+=j
    else:
        sum_o+=j

print(sum_e, sum_o)
#---------------------
lst = [ k for k in range(1,11)]
for d in range(len(lst)):
    print(lst[d]**2)
#---------------------
for m in range(1,21):
    print(m)


