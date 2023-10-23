def menu ():
    print('Operasi:'.center(36,'='))
    operasi = ['penjumlahan', 'pengurangan', 'perkalian', 'pembagian', 'pembagian bulat']
    for i in range (len(operasi)):
        print(f'[{i+1}]. {operasi[i].upper()}')
    else:
        print("[6]. EXIT")
    choose = input('pilih operasi:')
    
    if choose.lower() == 'penjumlahan' or choose == '1':
        penjumlahan()
    elif choose.lower() == 'pengurangan' or choose == '2':
        pengurangan()
    elif choose.lower() == 'perkalian' or choose == '3':
        perkalian()
    elif choose.lower() == 'pembagian' or choose == '4':
        pembagian()
    elif choose.lower() == 'pembagian bulat' or choose == '5':
        pembagian_bulat()
    elif choose.lower() == 'exit' or choose == '6':
        exit ()
    else:
        print('Operasi tidak tersedia')
        
    if __name__ == "__main__":
        menu()

def penjumlahan ():
    print('Penjumlahan'.center(36,'='))
    a = float(input('Masukkan angka pertama: '))
    b = float(input('Masukkan angka kedua: '))
    print(f'{a} + {b} = {a+b}')
    print('='*36)

def pengurangan ():
    print('Pengurangan'.center(36,'='))
    a = float(input('Masukkan angka pertama: '))
    b = float(input('Masukkan angka kedua: '))
    print(f'{a} - {b} = {a-b}')
    print('='*36)

def perkalian ():
    print('Perkalian'.center(36,'='))
    a = float(input('Masukkan angka pertama: '))
    b = float(input('Masukkan angka kedua: '))
    print(f'{a} x {b} = {a*b}')
    print('='*36)

def pembagian ():
    print('Pembagian'.center(36,'='))
    a = float(input('Masukkan angka pertama: '))
    b = float(input('Masukkan angka kedua: '))
    print(f'{a} : {b} = {a/b}')
    print('='*36)

def pembagian_bulat ():
    print('Pembagian Bulat'.center(36,'='))
    a = float(input('Masukkan angka pertama: '))
    b = float(input('Masukkan angka kedua: '))
    print(f'{a} // {b} = {a//b}')
    print('='*36)

menu()