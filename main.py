from random import randrange


x = randrange(101)
dnm = 0

while True:
    try:
        y = int(input("Please write number between 0 and 100!\n"))

    except ValueError:
        print("Please only write a number!")
        continue

    if(x==y):
        print("Found it!\n")
        dnm=+ dnm+ 1
        break
    elif(x>y):
        print("Up!")
        dnm=+ dnm+1
    elif(x<y):
        print("Down!")
        dnm=+ dnm +1


print("{} deneme sonrası buldunuz".format(dnm))