import json
import csv

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
    for i in data:
        if (data[count]['jud'] == data[count]['cjud']):
            data[count].update(result = 1) #Добавляем информацию о правильности ответа
        else:
            data[count].update(result = 0) #Добавляем информацию о неправильности ответа
        writer.writerow((data[count])) #Записываем строку
        count += 1

