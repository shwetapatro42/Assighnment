# que 1
from itertools import combinations
S,k=input().split()
for i in range(1,int(k)+1):
    for j in combinations(sorted(S),i):
        print("".join(j))

# que 2
from itertools import product 
a = map(int, input().split())
b = map(int, input().split())
print(*product(a, b))

# que 3
from itertools import permutations
string, length = input().split()
output = ["".join(i) for i in permutations(string,int(length))]
output.sort()
print("\n".join(output))