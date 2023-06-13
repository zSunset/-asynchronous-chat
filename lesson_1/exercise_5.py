from subprocess import PIPE, Popen
import chardet

my_list = ['ping', 'yandex.ru']
my_list_2 = ['ping', 'youtube.com']

data_ping = Popen(my_list,stdout=PIPE)
data_ping_2 = Popen(my_list_2,stdout=PIPE)

for i in data_ping.stdout:
    print(chardet.detect(i))
    print(i.decode('ASCII'))

for i in data_ping_2.stdout:
    print(chardet.detect(i))
    print(i.decode('ASCII'))