age = int(input("Quel age avez-vouz?"))
if age > 18:
    print('Vouz est majeur')
if age < 18:
    print('Vous est mineur')

    
a=1
while a<=10:
    b=1
    while b<=a:
        c=a*b
        print(c, end=" ")
        b+=1
    print(" ")
    a+=1

