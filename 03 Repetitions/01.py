n = input() 
l = len(n)
max_ctr = 1
ctr = 1
for i in range(1, l):
    if n[i] == n[i-1]:
        ctr += 1 
    else: 
        ctr = 1
    max_ctr = max(ctr, max_ctr)
print(max_ctr)
