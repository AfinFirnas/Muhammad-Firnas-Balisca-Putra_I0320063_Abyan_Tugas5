# Program Grading Nilai

Nama = str(input('Masukkan Nama Anda : '))
Nilai = int(input('Masukkan Nilai Anda : '))

if Nilai < 60 :
    print('Halo,', Nama ,'!', 'Nilai Anda setelah dikonversi adalah E')
elif 60 <= Nilai <= 64 :
    print('Halo,', Nama ,'!', 'Nilai Anda setelah dikonversi adalah C')
elif 65 <= Nilai <= 69 :
    print('Halo,', Nama, '!', 'Nilai Anda setelah dikonversi adalah C+')
elif 70 <= Nilai <= 74 :
    print('Halo,', Nama, '!', 'Nilai Anda setelah dikonversi adalah B')
elif 75 <= Nilai <= 79 :
    print('Halo,', Nama, '!', 'Nilai Anda setelah dikonversi adalah B+')
elif 80 <= Nilai <= 84 :
    print('Halo,', Nama, '!', 'Nilai Anda setelah dikonversi adalah A-')
elif 85 <= Nilai <= 100 :
    print('Halo,', Nama, '!', 'Nilai Anda setelah dikonversi adalah A')
else:
    print('Nilai Tidak Valid!')