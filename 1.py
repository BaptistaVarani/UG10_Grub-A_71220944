a=str(input('masukan nama mahasiswa:'))
b=str(input('masukan NIM-nya:'))
if b(0:2)=='71' and int(b[2:4])<=22 and int(b[2:4])>=20:
    print(f'{a},'merupakan mahasiswa informatika angkatan 20 hingga 22')
else:
    print(f'{a},'bukan mahasiswa informatika angkatan 20 hingga 22')
