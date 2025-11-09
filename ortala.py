def ortala(b, sayac):
    dizi = []

    while sayac > 0:
        kare = b * b
        usayi = str(kare)

        
        while len(usayi) < 2 * len(str(b)):
            usayi = '0' + usayi

        orta = len(usayi) // 2
        ys = usayi[orta - len(str(b)) // 2: orta + len(str(b)) // 2]

        b = int(ys)
        dizi.append(b)

        sayac -= 1

    return dizi



rastgele = ortala(1234, 5)
print(rastgele)