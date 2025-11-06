
#Ülesanne 3

import random

õiged = 0

for i in range(10):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    tulemus = a + b
    print(f"{a} + {b} = ?")

    for katse in range(5):
        vastus = int(input())
        if vastus == tulemus:
            print("Õige!")
            õiged += 1
            break
        else:
            if katse == 4:
                print(f"Kaotasid! Õige vastus oli {tulemus}.")
            else:
                print("Vale, proovi uuesti!")

print(f"Õiged vastused: {õiged}/10")

#Ülesanne 4

for i in range(1, 11):
    print(i)

#Ülesanne 7

import random

for i in range(5):
    print(random.randint(0, 9), end='')

#Ülesanne 10

for arv in range(1, 101):
    if arv % 5 == 0:
        print(arv)

#Ülesanne 14

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()

#Ülesanne 15

katseid = 0

while True:
    vastus = input("Osta elevant ära! ").lower()
    katseid += 1

    if vastus == "elevant":
        print(f"Lõpuks! Sa ütlesid 'elevant'. Küsimust küsiti {katseid} korda.")
        break

#Ülesanne 22

katseid = 0

while True:
    vastus = input("Tahan kommi! ").lower()
    katseid += 1

    if vastus == "komm":
        print(f"Lõpuks! Sa ütlesid 'komm'. Küsimust küsiti {katseid} korda.")
        break
