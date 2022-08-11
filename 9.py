def print_hellow(name):
    if name != "michael":
        print(f"hello {name}")


def greet_name(name, excluded_name="michael", greeting_word="hellow"):
    if name != excluded_name:
        print(f"{greeting_word} {name}")


def multiply(x, y):
    result = x * y
    return result


print_hellow("moshe")
print_hellow("david")
bla = multiply(10, 4)
if bla > 38:
    print("ok")
greet_name("moshe")

user_name = input("enter your name: ")
greet_name(user_name)

