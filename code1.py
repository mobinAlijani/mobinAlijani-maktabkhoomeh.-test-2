import random
x=1
y=99
hads = random.randint(x,y)
print(hads)
javob = input()

while javob != "d":

    if javob == "k":
        y = hads-1
        hads = random.randint(x,y)
        print(hads)
    elif javob == "b":
        x = hads+1
        hads = random.randint(x,y)
        print(hads)
    javob = input()
    
