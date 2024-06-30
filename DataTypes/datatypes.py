

print("------- Numeric types -------")
x = 50
print(f"{type(x)} : {x}")
x = 60.5
print(f"{type(x)} : {x}")
x = 2 + 3j
print(f"{type(x)} : {x}")

print("------- Sequence types -------")
x = "Hello World"
print(f"{type(x)} : {x}")
x = ["geeks", "for", "geeks"]
print(f"{type(x)} : {x}")
x = ("geeks", "for", "geeks")
print(f"{type(x)} : {x}")
x = range(10)
print(f"{type(x)} : {x}")

print("------- Dictionary types -------")
x = {"name": "Suraj", "age": 24}
print(f"{type(x)} : {x}")

print("------- Set types -------")
x = {"geeks", "for", "geeks"}
print(f"{type(x)} : {x}")
x = frozenset({"geeks", "for", "geeks"})
print(f"{type(x)} : {x}")

print("------- Binary types -------")
x = b"Geeks"
print(f"{type(x)} : {x}")
x = bytearray(4)
print(f"{type(x)} : {x}")
x = memoryview(bytes(6))
print(f"{type(x)} : {x}")

print("------- Others types -------")
x = True
print(f"{type(x)} : {x}")
x = None
print(f"{type(x)} : {x}")
