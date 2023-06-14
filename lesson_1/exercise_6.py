from chardet.universaldetector import UniversalDetector
my_list = ['сетевое программирование', 'сокет', 'декоратор']

detector = UniversalDetector()

with open('data.txt', 'rb') as data:
    for datas in data:
        detector.feed(datas)
        if detector.done:
            break
    detector.close()
print(detector.result)

with open('data.txt', 'r', encoding='UTF-8') as file:
    content = file.read()
    print(content)