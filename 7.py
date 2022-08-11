#7 boom
for i in range (101):
    if i % 7 == 0 or i % 10 == 7:
        continue
    print(i)
else:
    print("loop finished successfully")
