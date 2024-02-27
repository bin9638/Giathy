


mod = int(1e9+7)

with open('A.inp', 'r') as file:
    #n=int(input())
    n = int(file.read())
  #  n=3
with open('A.out', 'w') as file:
    file.write(str(((n-2)*(n-1)//2 + n // 2-(n % 2 == 0))//2%mod))



