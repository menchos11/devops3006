#2
try:
#1
    a = 1/0
except Exception as e:
    print(e)
#3 (yes)
try:
    x = 1
finally:
    print("finally")
#4 any exception
#5 its says only that there is an exception and not the reason
#6 the excepions that can be caught is input/output errors or division whith zero
#7
my_file = open("words.txt", 'w')
#8
my_file.write("menachem")
my_file.close()
#9
my_file = open("words.txt", 'r')
file_cont = my_file.read()
print(file_cont)
my_file.close()
#10
heb_file = open("hebrew", 'w', encoding="utf16")
heb_file.write("מנחם")
heb_file.close()
heb_file = open("hebrew", 'r', encoding="utf16")
heb = heb_file.read()
print(heb)
heb_file.close()