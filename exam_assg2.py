# que 1
cube = lambda x: x ** 3
def fibonacci(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
if _name_ == '_main_':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# que 2
if _name_ == '_main_':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = [];
    abc = [];
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z];
                    output.append(abc);
print(output);    

# que 3
Regex_Pattern = r'hackerrank'   # Do not delete 'r'.
import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# que 4
Regex_Pattern = r"^\d\S{4}\.$"  # Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# que 5
Regex_Pattern = r'hackerrank'   # Do not delete 'r'.
import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# que 6
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z].*'   # Do not delete 'r'.
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())