file_name = 'poem.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end="")
print(file.closed)
print('При завершении работы оператора with файл автоматически закрывается')
