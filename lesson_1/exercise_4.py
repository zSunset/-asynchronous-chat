my_list = ['разработка', 'администрирование', 'protocol', 'standard']
for i in my_list:
    enc = bytes(i, encoding='UTF-8')
    print(enc)
    dec = enc.decode('UTF-8')
    print(type(dec))