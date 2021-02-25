sum = 0
print("Programma â€žKÄ� rÅ«pÄ“ties par bruÅ†urupuci?â€� Tev palÄ«dzÄ“s saprast un atcerÄ“ties, kas jÄ�zina pirms pieskata bruÅ†urupuci.")
print("Tev tiks uzdoti 10 jautÄ�jumi, ar kuru palÄ«dzÄ«bu spÄ“si novÄ“rtÄ“t, vai esi gatavs uzÅ†emties rÅ«pes.")
print("No piedÄ�vÄ�tajiem atbilÅ¾u variantiem, izvÄ“lies vienu un ieraksti atbilstoÅ¡o ciparu.")
print("Cik bieÅ¾i jÄ�baro bruÅ†urupucis?")
print("1. 3 reizes dienÄ�")
print("2. Reizi dienÄ�")
print("3. Reizi nedÄ“Ä¼Ä�") 
print("4. 6 reizes nedÄ“Ä¼Ä�")
a=int(input("1. jautÄ�juma atbilde - "))
if a==4: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 4. 6 reizes nedÄ“Ä¼Ä�.")
if a==4:
    sum=sum+1
print("No kÄ� sastÄ�v bruÅ†urupuÄ�a pamatuzturs?")
print("1. No tÄ�, ko Ä“d cilvÄ“ks")
print("2. Augu produktiem")
print("3. GaÄ¼u, zivÄ«m")
print("4. Tikai augÄ¼iem")
b=int(input("2. jautÄ�juma atbilde - "))
if b==2: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 2. Augu produktiem .")
if b==2:
    sum=sum+1
print("Vai bruÅ†urupucim vajadzÄ«gi vitamÄ«ni?")
print("1. JÄ�")
print("2. NÄ“")
print("3. Tikai tad, ja tas ir saslimis")
c=int(input("3. jautÄ�juma atbilde - "))
if c==1: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 1. BruÅ†urupucim nepiecieÅ¡ami vitamÄ«ni arÄ« ikdienÄ�, tÄ�pat kÄ� mums, cilvÄ“kiem .")
if c==1:
    sum=sum+1
print("Kas no minÄ“tÄ� bruÅ†urupucim ir vajadzÄ«gs?")
print("1. TerÄ�rijs")
print("2. SildoÅ¡Ä� lampa")
print("3. Smiltis")
print("4. Viss iepriekÅ¡ minÄ“tais")
d=int(input("4. jautÄ�juma atbilde - "))
if d==4: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 4. BruÅ†urupucim nepecieÅ¡ams viss iepriekÅ¡ minÄ“tais .")
if d==4:
    sum=sum+1
print("Ko bruÅ†urupuÄ�i dara ziemÄ�?")
print("1. GuÄ¼ ziemas miegu ")
print("2. Ä’d vairÄ�k pÄ�rtikas ")
print("3. Ir Ä¼oti aktÄ«vi")
print("4. - To paÅ¡u, ko citos gadalaikos")
e=int(input("5. jautÄ�juma atbilde - "))
if e==4: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 1. BruÅ†urupucim nepiecieÅ¡ams atpÅ«tas laiks - ziemas miegs .")
if e==4:
    sum=sum+1
print("Cik bieÅ¾i bruÅ†urupucis jÄ�mazgÄ�?")
print("1. Reizi dienÄ�")
print("2. Reizi nedÄ“Ä¼Ä�")
print("3. Katru otro dienu")
print("4. Tad, kad palicis netÄ«rs")
f=int(input("6. jautÄ�juma atbilde - "))
if f==2: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 2. BruÅ†urupucis jÄ�mazgÄ� reizi nedÄ“Ä¼Ä� .")
if f==2:
    sum=sum+1
print("1. TrauksmainÄ«ba")
print("2. KoÅ¡ana cilvÄ“kam")
print("3. AtteikÅ¡anÄ�s no pÄ�rtikas")
print("4. Visi iepriekÅ¡ minÄ“tie")
g=int(input("7. jautÄ�juma atbilde - "))
if g==3: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 3. Ja bruÅ†urupucis ilgu laiku atsakÄ�s no pÄ�rtikas .")
if g==3:
    sum=sum+1
print("Ko nedrÄ«kst dot bruÅ†urupucim?")
print("1. Dzert Å«deni")
print("2. AugÄ¼us")
print("3. Kalciju")
print("4. GaÄ¼u")
h=int(input("8. jautÄ�juma atbilde - "))
if h==1: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 1. Lai arÄ«, cik dÄ«vaini tas neliktos, bruÅ†urupucim nedrÄ«kst dot dzert Å«deni .")
if h==1:
    sum=sum+1
print("Ar kÄ�du lampu bruÅ†urupucis jÄ�silda?")
print("1. Ultravioletu staru")
print("2. Infrasarkano staru")
print("3. AbÄ�m minÄ“tajÄ�m")
i=int(input("9. jautÄ�juma atbilde - "))
if i==3: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 3. BruÅ†urupucim nepecieÅ¡amas abas lampas.")
if i==2:
    sum=sum+1    
print("Kas ir interesants par bruÅ†urupuÄ�u uzbÅ«vi?")
print("1. Nav ribas ")
print("2. Nav mÄ“les")
print("3. Nav zobu")
print("4. Viss iepriekÅ¡ minÄ“tais")
j=int(input("10. jautÄ�juma atbilde - "))
if j==3: print("Malacis!")
else: print("NÄ“! PareizÄ� atbilde ir 3. BruÅ†urupucim nav zobu .")
if j==3:
    sum=sum+1    
print("tavs rezultats -", sum)
if sum<=3: print("Mēģini vēlreiz")
elif 8>sum<=4: print("Tavas zināšanas ir videvējas, vēl jāatkarto zināšanas.")
else: print("Malacis, tu esi gatavs uzņemties rūpes par bruņurupuci.")