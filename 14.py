import ast
my_file = open("config.json")
c = dict(ast.literal_eval(my_file.read()))
if c["name"] == "aviel":
    print("i love devops")


with open("names.txt") as my_file:
    for name in my_file.readlines():
        print(name.strip())