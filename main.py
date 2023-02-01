from package1 import file1
import package1.file2
from package1.file2 import h

temp = file1.a
value = package1.file2.d

print(temp)
print(*value)
print(h)

import package1

print(package1.file1.c)