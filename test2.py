import random 

pole = [] 
delka = []
body = 0
body = int(body)


for i in range(random.randint(1, 15)):
    
    
    print("Kolo č.", i+1)
    

    for j in range(random.randint(1, 10)):
       pole.append(random.randint(1, 10))
 
    print(pole)
    

    delka = int(len(pole))
    

    odpoved = input("napiš délku pole v tomto kole hry:")
    odpoved = int(odpoved)

   

    if odpoved == delka:
        body = body + 1
        print("Správně, získáváš bod, tvé body: ", body)
    else:
        body = body - 1
        print("Špatně, ztrácíš bod, tvé body:", body)

print("-_- GAMER OVER -_-, tvé body", body)