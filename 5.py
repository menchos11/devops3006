is_true = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
names = ["chanan", "tom", "zack", "aharon"]
other_list = []
print(type(a == b))
if a < b and (b != 1) or not strOne == "moshe":
    print("a is smaller then b")
elif a == b:
    print("a equals b")
elif b>1:
    print("blabla")
else:
    print("something")
name_to_find = "ariel"
if name_to_find in names:
    print(f"we found {name_to_find}")
if len(other_list) > 0:
    print("other list has values")
k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
print(k == f)
print(k is f)
print(t == e)
print(t is e)
