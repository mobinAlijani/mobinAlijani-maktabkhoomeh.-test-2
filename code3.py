c = 0
vorodi = 0
jame = 0

for x in range(1,31):
    vorodi = int(input())
    if vorodi == 3:
         c = c + 1
    jame = vorodi + jame

print(jame,c)