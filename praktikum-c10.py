import os

def judul ():
    os.system('clear')
    print('PROGRAM PENGHITUNG VOLUME DAN LUAS PERMUKAAN ')
    print('BAGIAN RUANG BALOK')
    print()

def inputan():
    p =float(input('Masukkan Panjang: '))
    l =float(input('Masukkan Lebar: '))
    t =float(input('Masukkan Tinggi: '))
    return p,l,t


def perhitungan(p,l,t):
    vol = p * l * t
    luas = 2 * (p*l + p*t + l*t)
    luas_non_tutup = luas - p*l 
    return vol,luas,luas_non_tutup

def tampilkan(jenis,nilai):
    print(f'Nilai dari {jenis} adalah : {nilai}')

a = True
while a:
    # judul
    judul()

    # inputan
    p,l,t = inputan()

    # perhitungan
    vol,luas,luas_non_tutup = perhitungan(p,l,t)

    # tampilkan
    tampilkan('volume',vol)
    tampilkan('luas permukaan',luas)
    tampilkan('luas permukaan tanpa tutup',luas_non_tutup)

    # pilihan 
def pilihan():
    pilih = input('Apakah lanjutkan? [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Sampai jumpa lagi.')
    return a

def main():
    judul()                                      # judul
    p,l,t = inputan()                            #inputan
    vol,luas,luas_non_tutup = perhitungan(p,l,t) # perhitungan
    # tampilkan 
    tampilkan('volume',vol)
    tampilkan('luas permukaan',luas)
    tampilkan('luas permukaan tanpa tutup',luas_non_tutup)

a = True
while a:
    main()
    








