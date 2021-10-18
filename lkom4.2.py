print("@@@@@   @@@@@@   @@@@@   @@@@@@   @    @")
print("@       @    @   @       @    @   @    @")
print("@ @@@   @@@@@@   @ @@@   @@@@@@   @@@@@@")
print("@   @   @    @   @   @   @    @   @    @")
print("@@@@@   @    @   @@@@@   @    @   @    @")
aku=0
while aku==0:
    k=input('masukan list angka: ')
    # nilai di dalam K yang diberi spasi # 3 5 9
    genap=[]
    ganjil=[]
    for k in k.split():
        if int(k)%2==0:
                genap.append(int(k))
                print(' terdapat bilangan genap')
                break
        elif int(k)%2==0:
            genap.append(int(k))
            if int(k)%2==0:
                    print('terdapat bilangan genap')
                    break
        elif int(k)%2==1:
            print(' tidak terdapat bilangan genap')
            break
            
        else: 
            if int(k)%2==0:
                genap.append(int(k))
                print(' terdapat bilangan genap')

            
