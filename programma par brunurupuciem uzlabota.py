sum = 0
x = 0
print("Programma �K� rup�ties par sauszemes bru�urupuci?� Tev pal�dzes saprast un atcer�ties, kas j�zina pirms pieskata bru�urupuci.")
print("K�das ir tavas zin��anas par bru�urupu�iem?")
print("1. Zinu visu par bru�urupu�iem, v�los tikai atsvaidzin�t zin��anas")
print("2. Manas zin��anas ir da��jas par bru�urupu�iem")
print("3. Nezinu neko par bru�urupu�iem, ta�u v�los uzzin�t")
y=int(input("Savas zin��anas nov�rt�ju ar - "))
print("Tev tiks uzdoti 10 jaut�jumi, ar kuru pal�dz�bu sp�si nov�rt�t, vai esi gatavs uz�emties r�pes.")
print("No pied�v�tajiem atbil�u variantiem, izv�lies vienu un ieraksti atbilsto�o ciparu.")
while sum<8:
 sum = 0
 print("Cik bie�i j�baro bru�urupucis")
 print("1. 3 reizes dien�")
 print("2. Reizi dien�")
 print("3. Reizi ned���") 
 print("4. 6 reizes ned���")
 a=int(input("1. jaut�juma atbilde - "))
 if a==4:
  print("Malacis!")
  sum=sum+1
 if x==1 and a!=4: print("N�!")
 if x==0 and a!=4: print("N�! Pareiz� atbilde ir 4. 6 reizes ned���.")
 print("No k� sast�v bru�urupu�a pamatuzturs?")
 print("1. T�da pa�a, ko �d cilv�ks")
 print("2. Augu produktiem")
 print("3. Ga�u, ziv�m")
 print("4. Tikai aug�iem")
 b=int(input("2. jaut�juma atbilde - "))
 if b==2:
  print("Malacis!")
  sum=sum+1
 if x==1 and b!=2: print("N�!")
 if x==0 and a!=2: print("N�! Pareiz� atbilde ir 2. Augu produktiem .")
 print("Vai bru�urupucim vajadz�gi vitam�ni?")
 print("1. J�")
 print("2. N�")
 print("3. Tikai tad, ja tas ir saslimis")
 c=int(input("3. jaut�juma atbilde - "))
 if c==1:
  print("Malacis!")
  sum=sum+1
 if x==1 and c!=1: print("N�!")
 if x==0 and c!=1: print("N�! Pareiz� atbilde ir 1. Bru�urupucim nepiecie�ami vitam�ni ar� ikdiena, t�pat k� mums, cilv�kiem.")    
 print("Kas no min�ta bru�urupucim ir vajadz�gs?")
 print("1. Ter�rijs")
 print("2. Sildo�� lampa")
 print("3. Smiltis")
 print("4. Viss iepriek� min�tais")
 d=int(input("4. jaut�juma atbilde - "))
 if d==4: 
  print("Malacis!")
  sum=sum+1
 if x==1 and d!=4: print("N�!")
 if x==0 and d!=4: print("N�! Pareiz� atbilde ir 4. Bru�urupucim nepecie�ams viss iepriek� min�tais .")    
 print("Ko bru�urupu�i dara ziem�?")
 print("1. Gu� ziemas miegu ")
 print("2. �d vair�k p�rtikas ")
 print("3. Ir �oti akt�vi")
 print("4. To pa�u, ko citos gadalaikos")
 e=int(input("5. jaut�juma atbilde - "))
 if e==1: 
  print("Malacis!")
  sum=sum+1
 if x==1 and e!=1: print("N�!")
 if x==0 and e!=1: print("N�! Pareiz� atbilde ir 1. Bru�urupucim nepiecie�ams atp�tas laiks - ziemas miegs .")   
 print("Cik bie�i bru�urupucis j�mazg�?")
 print("1. Reizi dien�")
 print("2. Reizi ned���")
 print("3. Katru otro dienu")
 print("4. Tad, kad palicis net�rs")
 f=int(input("6. jautajuma atbilde - "))
 if f==2:
  print("Malacis!")
  sum=sum+1
 if x==1 and f!=2: print("N�!")
 if x==0 and f!=2: print("N�! Pareiz� atbilde ir 2. Bru�urupucis j�mazg� reizi ned��� .")   
 print("Kada viena no pirmaj�m slim�bas paz�mem bru�urupucim??")
 print("1. Trauksmain�ba")
 print("2. Ko�ana cilv�kam")
 print("3. Atteik�an�s no p�rtikas")
 print("4. Visi iepriek� min�tie")
 g=int(input("7. jaut�juma atbilde - "))
 if g==3: 
  print("Malacis!")
  sum=sum+1
 if x==1 and g!=3: print("N�!")
 if x==0 and g!=3: print("N�! Pareiz� atbilde ir 3. Jo bru�urupucis ilgu laiku atsak�s no p�rtikas .")
 print("Ko nedr�kst dot bru�urupucim?")
 print("1. Dzert �deni")
 print("2. Aug�us")
 print("3. Kalciju")
 print("4. Ga�u")
 h=int(input("8. jaut�juma atbilde - "))
 if h==1:
  print("Malacis!")
  sum=sum+1
 if x==1 and h!=1: print("N�!")
 if x==0 and h!=1: print("N�! Pareiz� atbilde ir 1. Lai ar�, cik d�vaini tas neliktos, bru�urupucim nedr�kst dot dzert �deni .")
 print("Ar k�du lampu bru�urupucis j�silda?")
 print("1. Ultravioletu staru")
 print("2. Infrasarkano staru")
 print("3. Ab�m min�taj�m")
 i=int(input("9. jaut�juma atbilde - "))
 if i==3: 
  print("Malacis!")
  sum=sum+1  
 if x==1 and i!=3: print("N�!")
 if x==0 and i!=3: print("N�! Pareiz� atbilde ir 3. Bru�urupucim nepecie�amas abas lampas.")
 print("Kas ir interesants par bru�urupu�u uzb�vi?")
 print("1. Nav ribas ")
 print("2. Nav m�les")
 print("3. Nav zobu")
 print("4. Viss iepriek� min�tais")
 j=int(input("10. jaut�juma atbilde - "))
 if j==3:
  print("Malacis!")
  sum=sum+1
 if x==1 and j!=3: print("N�!")
 if x==0 and j!=3: print("N�! Pareiz� atbilde ir 3. Bru�urupucim nav zobu.")
 print("tavs rezul�ts -", sum, "punkti")
 if sum==8 or sum==9 or sum==10: print("Malacis, tu esi gatavs uz�emties r�pes par bru�urupuci.")
 elif sum==4 or sum==5 or sum==6 or sum==7: print("Tavas zin��anas ir viduv�jas, vel j�atk�rto inform�cija.")
 else: print("M��ini v�lreiz.")
 print("Savu s�kotn�jo rezult�tu nor�diji ar",y,"l�meni, p�c testa tavs rezult�ts ir",sum, "punkti")
 x=1