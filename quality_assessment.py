import json
import csv
import pandas as pd


#Открываем CSV файл
with open('data_task3.csv') as data_csv:
    reader = csv.DictReader(data_csv, delimiter='\t')
    rows = list(reader)

#Записываем в JSON для удобства
with open('data_task3.json', 'w') as data_json:
    json.dump(rows, data_json)

#Открывает в режиме чтения JSON
with open("data_task3.json", "r") as data_json:
    data = json.load(data_json)

count = 0 #Счётчик

with open('data_task13.csv', "w") as data13_csv: #Открываем для записи
    writer = csv.DictWriter(data13_csv, fieldnames= ['login', 'uid', 'docid', 'jud', 'cjud', 'result']) #Даём понять что куда
    writer.writerow(({'login': 'login', 'uid': 'uid', 'docid': 'docid', 'jud': 'jud', 'cjud': 'cjud', 'result': 'result'})) #Подписываем столбцы
    for i in data:
        if (data[count]['jud'] == data[count]['cjud']):
            data[count].update(result = 1) #Добавляем информацию о правильности ответа
        else:
            data[count].update(result = 0) #Добавляем информацию о неправильности ответа
        writer.writerow((data[count])) #Записываем строку
        count += 1

data = pd.read_csv('data_task13.csv')
print(data)
print(len(data))
print(data[data['cjud'] > 0]) #29980 правильных ответов были «1». Значит 220 020 (88%) правильных ответов cjud — «0»
print(data[data['cjud'] < 1]) #Проверяем. Действительно, 220 020 cjud это «0»
print(data.groupby('uid').sum().sort_values(by=['result'])) #асессор с uid 234 набрал 48 правильных ответов, а асессор с uid 191 набрал 446
print(data[data['result'] == 0].groupby('uid').count().sort_values(by=['result'])) #Асессор с uid 56 справился хуже всех — 236 неправильных ответов
print(data[data['uid'] == 56][data['result'] == 1].groupby('uid').count().sort_values(by=['result'])) #175 верных ответов (42.5%) было у асессора с uid 56
print(data[data['uid'] == 191][data['result'] == 0].groupby('uid').count().sort_values(by=['result'])) #38 ошибок у асессора с uid 191. Меньше всего ошибок у 184 асессора, но в процентом соотношении лучший 191.

