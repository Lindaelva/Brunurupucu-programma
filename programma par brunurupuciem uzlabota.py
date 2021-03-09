sum = 0
x = 0
print("Programma „Kâ rupçties par sauszemes bruòurupuci?” Tev palçdzes saprast un atcerçties, kas jâzina pirms pieskata bruòurupuci.")
print("Kâdas ir tavas zinâðanas par bruòurupuèiem?")
print("1. Zinu visu par bruòurupuèiem, vçlos tikai atsvaidzinât zinâðanas")
print("2. Manas zinâðanas ir daïçjas par bruòurupuèiem")
print("3. Nezinu neko par bruòurupuèiem, taèu vçlos uzzinât")
y=int(input("Savas zinâðanas novçrtçju ar - "))
print("Tev tiks uzdoti 10 jautâjumi, ar kuru palîdzîbu spçsi novçrtçt, vai esi gatavs uzòemties rûpes.")
print("No piedâvâtajiem atbilþu variantiem, izvçlies vienu un ieraksti atbilstoðo ciparu.")
while sum<8:
 sum = 0
 print("Cik bieþi jâbaro bruòurupucis")
 print("1. 3 reizes dienâ")
 print("2. Reizi dienâ")
 print("3. Reizi nedçïâ") 
 print("4. 6 reizes nedçïâ")
 a=int(input("1. jautâjuma atbilde - "))
 if a==4:
  print("Malacis!")
  sum=sum+1
 if x==1 and a!=4: print("Nç!")
 if x==0 and a!=4: print("Nç! Pareizâ atbilde ir 4. 6 reizes nedçïâ.")
 print("No kâ sastâv bruòurupuèa pamatuzturs?")
 print("1. Tâda paða, ko çd cilvçks")
 print("2. Augu produktiem")
 print("3. Gaïu, zivîm")
 print("4. Tikai augïiem")
 b=int(input("2. jautâjuma atbilde - "))
 if b==2:
  print("Malacis!")
  sum=sum+1
 if x==1 and b!=2: print("Nç!")
 if x==0 and a!=2: print("Nç! Pareizâ atbilde ir 2. Augu produktiem .")
 print("Vai bruòurupucim vajadzîgi vitamîni?")
 print("1. Jâ")
 print("2. Nç")
 print("3. Tikai tad, ja tas ir saslimis")
 c=int(input("3. jautâjuma atbilde - "))
 if c==1:
  print("Malacis!")
  sum=sum+1
 if x==1 and c!=1: print("Nç!")
 if x==0 and c!=1: print("Nç! Pareizâ atbilde ir 1. Bruòurupucim nepiecieðami vitamîni arî ikdiena, tâpat kâ mums, cilvçkiem.")    
 print("Kas no minçta bruòurupucim ir vajadzîgs?")
 print("1. Terârijs")
 print("2. Sildoðâ lampa")
 print("3. Smiltis")
 print("4. Viss iepriekð minçtais")
 d=int(input("4. jautâjuma atbilde - "))
 if d==4: 
  print("Malacis!")
  sum=sum+1
 if x==1 and d!=4: print("Nç!")
 if x==0 and d!=4: print("Nç! Pareizâ atbilde ir 4. Bruòurupucim nepecieðams viss iepriekð minçtais .")    
 print("Ko bruòurupuèi dara ziemâ?")
 print("1. Guï ziemas miegu ")
 print("2. Çd vairðk pârtikas ")
 print("3. Ir ïoti aktîvi")
 print("4. To paðu, ko citos gadalaikos")
 e=int(input("5. jautâjuma atbilde - "))
 if e==1: 
  print("Malacis!")
  sum=sum+1
 if x==1 and e!=1: print("Nç!")
 if x==0 and e!=1: print("Nç! Pareizâ atbilde ir 1. Bruòurupucim nepiecieðams atpûtas laiks - ziemas miegs .")   
 print("Cik bieþi bruòurupucis jâmazgâ?")
 print("1. Reizi dienâ")
 print("2. Reizi nedçïâ")
 print("3. Katru otro dienu")
 print("4. Tad, kad palicis netîrs")
 f=int(input("6. jautajuma atbilde - "))
 if f==2:
  print("Malacis!")
  sum=sum+1
 if x==1 and f!=2: print("Nç!")
 if x==0 and f!=2: print("Nç! Pareizâ atbilde ir 2. Bruòurupucis jâmazgâ reizi nedçïâ .")   
 print("Kada viena no pirmajâm slimîbas pazîmem bruòurupucim??")
 print("1. Trauksmainîba")
 print("2. Koðana cilvçkam")
 print("3. Atteikðanâs no pârtikas")
 print("4. Visi iepriekð minçtie")
 g=int(input("7. jautâjuma atbilde - "))
 if g==3: 
  print("Malacis!")
  sum=sum+1
 if x==1 and g!=3: print("Nç!")
 if x==0 and g!=3: print("Nç! Pareizâ atbilde ir 3. Jo bruòurupucis ilgu laiku atsakâs no pârtikas .")
 print("Ko nedrîkst dot bruòurupucim?")
 print("1. Dzert ûdeni")
 print("2. Augïus")
 print("3. Kalciju")
 print("4. Gaïu")
 h=int(input("8. jautâjuma atbilde - "))
 if h==1:
  print("Malacis!")
  sum=sum+1
 if x==1 and h!=1: print("Nç!")
 if x==0 and h!=1: print("Nç! Pareizâ atbilde ir 1. Lai arî, cik dîvaini tas neliktos, bruòurupucim nedrîkst dot dzert ûdeni .")
 print("Ar kâdu lampu bruòurupucis jâsilda?")
 print("1. Ultravioletu staru")
 print("2. Infrasarkano staru")
 print("3. Abâm minçtajâm")
 i=int(input("9. jautâjuma atbilde - "))
 if i==3: 
  print("Malacis!")
  sum=sum+1  
 if x==1 and i!=3: print("Nç!")
 if x==0 and i!=3: print("Nç! Pareizâ atbilde ir 3. Bruòurupucim nepecieðamas abas lampas.")
 print("Kas ir interesants par bruòurupuèu uzbûvi?")
 print("1. Nav ribas ")
 print("2. Nav mçles")
 print("3. Nav zobu")
 print("4. Viss iepriekð minçtais")
 j=int(input("10. jautâjuma atbilde - "))
 if j==3:
  print("Malacis!")
  sum=sum+1
 if x==1 and j!=3: print("Nç!")
 if x==0 and j!=3: print("Nç! Pareizâ atbilde ir 3. Bruòurupucim nav zobu.")
 print("tavs rezulâts -", sum, "punkti")
 if sum==8 or sum==9 or sum==10: print("Malacis, tu esi gatavs uzòemties rûpes par bruòurupuci.")
 elif sum==4 or sum==5 or sum==6 or sum==7: print("Tavas zinâðanas ir viduvçjas, vel jâatkârto informâcija.")
 else: print("Mçìini vçlreiz.")
 print("Savu sâkotnçjo rezultâtu norâdiji ar",y,"lîmeni, pçc testa tavs rezultâts ir",sum, "punkti")
 x=1