# types of variable
strA = "Hello, World!"  # string
intB = 5                # str
floatC = 1.2            # float
boolD = True            # bool
# besides, variables can be a list or dictionary, but i will study another day

# print out
print("Hello, world!")
print(strA)
print(intB)
# print out with more than 1 type of variable
print(f"{strA}, hello {intB}")

# if else
if intB > 10:
    print("b > 10")
elif intB == 10:
    print("b = 10")
else:
    print("b < 10")

# for loop
for i in strA:
    print(i)

# while loop
i = 0
while i < 3:
    print(i)
    i += 1

# function (def)
def LessThan10(x):
    if x < 10:
        print("True")
    else:
        print("False")
LessThan10(intB)
