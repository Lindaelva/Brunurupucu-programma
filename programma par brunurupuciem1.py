sum = 0
print("Programma „Ka rupeties par sauszemes brunurupuci?” Tev palidzes saprast un atcereties, kas jazina pirms pieskata brunurupuci.")
print("Tev tiks uzdoti 10 jautaumi, ar kuru palidzibu spesi novertet, vai esi gatavs uznemties rupes.")
print("No piedavatajiem atbilzu variantiem, izvelies vienu un ieraksti atbilstoso ciparu.")
print("Cik biezi jābaro bruņurupucis")
print("1. 3 reizes diena")
print("2. Reizi diena")
print("3. Reizi nedela") 
print("4. 6 reizes nedela")
a=int(input("1. jautajuma atbilde - "))
if a==4: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 4. 6 reizes nedela.")
if a==4:
    sum=sum+1
print("No ka sastav brunurupuca pamatuzturs?")
print("1. Tadu pasu, ko ed cilveks")
print("2. Augu produktiem")
print("3. Galu, zivim")
print("4. Tikai augliem")
b=int(input("2. jautajuma atbilde - "))
if b==2: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 2. Augu produktiem .")
if b==2:
    sum=sum+1
print("Vai brunurupucim vajadzigi vitamini?")
print("1. Ja")
print("2. Ne")
print("3. Tikai tad, ja tas ir saslimis")
c=int(input("3. jautajuma atbilde - "))
if c==1: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 1. Brunurupucim nepieciesami vitamini ari ikdiena, tapat ka mums, cilvekiem.")
if c==1:
    sum=sum+1
print("Kas no mineta brunurupucim ir vajadzigs?")
print("1. Terarijs")
print("2. Sildosa lampa")
print("3. Smiltis")
print("4. Viss ieprieks minetais")
d=int(input("4. jautajuma atbilde - "))
if d==4: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 4. Brunurupucim nepeciesams viss ieprieks minetais .")
if d==4:
    sum=sum+1
print("Ko brunurupuci dara ziema?")
print("1. Gul ziemas miegu ")
print("2. Ed vairak partikas ")
print("3. Ir loti aktivi")
print("4. - To pasu, ko citos gadalaikos")
e=int(input("5. jautajuma atbilde - "))
if e==1: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 1. Brunurupucim nepieciesams atputas laiks - ziemas miegs .")
if e==1:
    sum=sum+1
print("Cik biezi brunurupucis jamazga?")
print("1. Reizi diena")
print("2. Reizi nedela")
print("3. Katru otro dienu")
print("4. Tad, kad palicis netirs")
f=int(input("6. jautajuma atbilde - "))
if f==2: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 2. Brunurupucis jamazga reizi nedela .")
if f==2:
    sum=sum+1
print("Kada viena no pirmajam slimibas pazimem brunurupucim??")
print("1. Trauksmainiba")
print("2. Kosana cilvekam")
print("3. Atteiksanas no partikas")
print("4. Visi ieprieks minetie")
g=int(input("7. jautajuma atbilde - "))
if g==3: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 3. Jo brunurupucis ilgu laiku atsakas no partikas .")
if g==3:
    sum=sum+1
print("Ko nedrikst dot brunurupucim?")
print("1. Dzert udeni")
print("2. Auglus")
print("3. Kalciju")
print("4. Galu")
h=int(input("8. jautajuma atbilde - "))
if h==1: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 1. Lai ari, cik divaini tas neliktos, brunurupucim nedrikst dot dzert udeni .")
if h==1:
    sum=sum+1
print("Ar kadu lampu brunurupucis jasilda?")
print("1. Ultravioletu staru")
print("2. Infrasarkano staru")
print("3. Abam minetajam")
i=int(input("9. jautauma atbilde - "))
if i==3: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 3. Brunurupucim nepeciesamas abas lampas.")
if i==3:
    sum=sum+1    
print("Kas ir interesants par brunurupucu uzbuvi?")
print("1. Nav ribas ")
print("2. Nav meles")
print("3. Nav zobu")
print("4. Viss ieprieks minetais")
j=int(input("10. jautajuma atbilde - "))
if j==3: print("Malacis!")
else: print("Ne! Pareiza atbilde ir 3. Brunurupucim nav zobu.")
if j==3:
    sum=sum+1    
print("tavs rezulats -", sum, "punkti")
if sum==8 or sum==9 or sum==10: print("Malacis, tu esi gatavs uznemties rupes par brunurupuci.")
elif sum==4 or sum==5 or sum==6 or sum==7: print("Tavas zinasanas ir viduveji, vel jaatkarto informacija.")
else: print("Megini velreiz.")
