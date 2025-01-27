def element_occ() :
   T = []
   for i in range (0,10) :
      a=input(f"enter l'element {i+1} : ")
      T.append(a)

   ele = None
   max_ = 0

   for i in range(len(T)):
      count = T.count(T[i])
    
      if count > max_:
         ele = T[i]
         max_ = count
   return ele

resultat = element_occ()
print(f"l'élément le plus occ est {resultat}")
      

