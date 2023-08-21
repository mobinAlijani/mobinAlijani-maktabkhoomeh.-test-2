x = 0
sen =int(input())
y = 0

while sen != -1 :
    if sen > x :
        y = x
        x = sen
    elif sen < x and sen > y :
        y = sen
    sen =int(input())   

print(x,y)
