import random

parola_uzunluğu = input('parola istiyorsanız evet yazın:')
rastgele_parola = random.randint(0,999999)

if parola_uzunluğu == 'evet':
    print(rastgele_parola)
else:
    print('yazdığıklarınızı kontrol ediniz')
