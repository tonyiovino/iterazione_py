num = input("Inserisci il numero dei termini da usare: ")
num = int(num)

divisore = 1
count = 0
pi_greco = 0
segno = 1

while count < num:
    pi_greco = pi_greco + segno * 4/divisore
    segno = - segno
    count+=1
    divisore+=2

print("Pi Greco:", pi_greco)