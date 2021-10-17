aku=0 #untuk loop
while aku == 0: #untuk loop

    print("@@@@@   @@@@@@   @@@@@   @@@@@@   @    @")
    print("@       @    @   @       @    @   @    @")
    print("@ @@@   @@@@@@   @ @@@   @@@@@@   @@@@@@")
    print("@   @   @    @   @   @   @    @   @    @")
    print("@@@@@   @    @   @@@@@   @    @   @    @\n")

    rif = input (' masukan list bilangan: ') #minta input
    genap = [] #menyiapkan list genap
    ganjil = [] #menyiapkan list ganjil
    for rif in rif.split(): #menggunakan split untuk spasi
        #conditional Statement
        if int(rif) %2==0: 
                genap.append(int(rif))
        #conditional Statement        
        else :
           ganjil.append(int(rif))
    #print hasil input
    print(f'{genap} terdapat bilangan genap')
    print(f'{ganjil} terdapat bilangan ganjil')
