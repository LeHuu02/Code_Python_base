
a = int(10)
def work():
    global a
    print("so a: ", a)
    a = 121
    # a = int("a")

work()
print("so sau a: ",a)