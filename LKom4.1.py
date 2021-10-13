import sys
a=0
while a ==0:
    print("=== PROGRAM KOVERSI BILANGAN===")
    print("1.Desimal ke Biner")
    print("2.Biner ke Desimal")
    print("3.Keluar")
    a1=int(input("silahkan Pilih Menu: "))
    if a1==1:
        desimal = int(input("masukan Desimal: "))
        if desimal ==0:
            print(0)
        else:
            print("hasil bagi sisa biner")
            bitstring=""
        while desimal > 0:
            sisa= desimal %2
            desimal = desimal//2
            bitstring= str(sisa) + bitstring
            
            print("Binernya adalah: ",bitstring)

    elif a1==2:
        bit=input("Masukan Str Binner: ")
        desimal=0
        eks = len(bit)-1
        for digit in bit:
            desimal += int(digit)*2**eks
            eks -= 1
        print ("Nilai Desimal adalah :",desimal)
    elif a1==3:
        sys.exit(0)
