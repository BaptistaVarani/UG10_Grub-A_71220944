print('===== selamat datang di toko Andi Tersenyum,Selamat belanja! =====')
a=int(input('total belanja rp:'))
if a<100000:
    print('biaya yang harus dibayar setelah diskon adalah:RP',a) 
elif a>=100000:
    print('biaya yang harus dibayar setelah diskon adalah:RP',a-(a*0.02))
elif a>=500000:
    print('biaya yang harus dibayar setelah diskon adalah:RP',a-(a*0.05))
elif a>=100000:
    print('biaya yang harus dibayar setelah diskon adalah:RP',a-(a*0.010))
else:
    print('beli apa kaka')
