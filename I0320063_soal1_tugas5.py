# Program untuk menyapa pengunjung

Nama = str(input('Masukkan Nama Anda : '))
Kelamin = str(input('Masukkan Jenis Kelamin Anda(L/P) : '))

if Kelamin == 'L' :
    print('Selamat datang,','Tuan', Nama,'!' )
elif Kelamin == 'P' :
    print('Selamat datang,', 'Nyonya', Nama, '!')