T=[]
S = int(input("combien de nombre voulez vous entrer : "))
for i in range (S) :
    nums=int(input(f"entrer le nombre {i+1} : "))
    T.append(nums)
target = int(input("entrer le nombre voulu : "))
for i in range(len(T)) :
    for j in range (i+1,len(T)):
        if target == T[i] + T[j] :
            z = i 
            k = j
            break
print("[", z , ",", k ,"]")