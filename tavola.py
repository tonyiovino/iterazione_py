colonna = 1
while colonna <= 10:
    riga = 1

    while riga <= 10:
        prodotto = riga * colonna

        print("%5d"% (prodotto), end="")

        riga+=1

    print("\n")
    colonna+=1