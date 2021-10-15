aku=0 #untuk loop
while aku == 0: #untuk loop

    print("@@@@@   @@@@@@   @@@@@   @@@@@@   @    @")
    print("@       @    @   @       @    @   @    @")
    print("@ @@@   @@@@@@   @ @@@   @@@@@@   @@@@@@")
    print("@   @   @    @   @   @   @    @   @    @")
    print("@@@@@   @    @   @@@@@   @    @   @    @\n")

    rifdah = input (' masukan list bilangan: ') #minta input
    genap = [] #menyiapkan list genap
    ganjil = [] #menyiapkan list ganjil
    for rifdah in rifdah.split(): #menggunakan split untuk spasi
        #conditional Statement
        if int(rifdah) %2==0: 
                genap.append(int(rifdah))
        #conditional Statement        
        else :
           ganjil.append(int(rifdah))
    #print hasil input
    print(f'{genap} terdapat bilangan genap')
    print(f'{ganjil} terdapat bilangan ganjil')