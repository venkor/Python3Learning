print("The Truth Terms:")
print("""and
or
not
!= (not equal)
== (equal)
>= (greater-than-equal)
<= (less-than-equal)
True
False
""")
print("Some Boolan algebra logic:")
print("The Truth Tables:\n-----------------------------",end = ' ')
print("""
NOT\t\tTrue?
not False\tTrue
not True\tFalse""")
print("-----------------------------")
print("""
OR\t\tTrue?
True or False\tTrue
True or True\tTrue
False or True\tTrue
False or False\tFalse
""")
print("-----------------------------")
print("""
AND\t\tTrue?
True and False\tFalse
True and True\tTrue
False and True\tFalse
False and False\tFalse
""")
print("-----------------------------")
print("""
NOT OR\t\t\tTrue?
not(True or False)\tFalse
not(True or True)\tFalse
not(False or True)\tFalse
not(False or False)\tTrue
""")
print("-----------------------------")
print("""
NOT AND\t\t\tTrue?
not(True and False)\tTrue
not(True and True)\tFalse
not(False and True)\tTrue
not(False and False)\tTrue
""")
print("-----------------------------")
print("""
!=\tTrue?
1 != 0\tTrue
1 != 1\tFalse
0 != 1\tTrue
0 != 0\tFalse
""")
print("-----------------------------")
print("""
==\tTrue?
1 == 0\tFalse
1 == 1\tTrue
0 == 1\tFalse
0 == 0\tTrue
""")
print("-----------------------------")
