a = "123"
b = "1.2"



print(f"a is decimal? {a.isdecimal()}")
print(f"a is numeric? {a.isnumeric()}")
print(f"a is digit? {a.isdigit()}")

# Essas funções builtin são problematicas em caso de float
print(f"b is decimal? {b.isdecimal()}")
print(f"b is numeric? {b.isnumeric()}")
print(f"b is digit? {b.isdigit()}")