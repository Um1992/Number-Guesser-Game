from random import randrange


x = randrange(101)
dnm = 0

while True:
    try:
        y = int(input("0 ile 100 arası bir sayı girin!\n"))

    except ValueError:
        print("Lütfen sadece sayı girin!")
        continue

    if(x==y):
        print("Bildiniz!\n")
        dnm=+ dnm+ 1
        break
    elif(x>y):
        print("Yukarı!")
        dnm=+ dnm+1
    elif(x<y):
        print("Aşağı!")
        dnm=+ dnm +1


print("{} deneme sonrası buldunuz".format(dnm))