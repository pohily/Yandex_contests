'''
Вывод статистики по country: country;sum(count) (сумма по count);count_uniq(user_id) (число уникальных user_id для country)

Без использования дополнительных библиотек структур данных и алгоритмов (то есть с базовыми типами, циклами и массивами. Словари, множества, хэш-таблицы уже считаются дополнительными структурами данных).
'''

with open('input.txt', 'r') as f:
    data = []
    for line in f:
        data.append(line.strip())

    user_id = []
    counts = []
    countrys = []
    for line in data:
        tmp = line.split(';')
        user = 0
        count = 0
        if len(tmp) == 3 and isinstance(tmp[2], str):       #type check
            country = tmp[2]
            try:                        
                user = int(tmp[0])
                count = int(tmp[1])
            except ValueError:
                continue

            if user and count:                              #adding data
                if country not in countrys:
                    countrys.append(country)
                    user_id.append([user])
                    counts.append(count)
                else:
                    index = countrys.index(country)
                    if user in user_id[index]:
                        counts[index] += count
                    else:
                        user_id[index].append(user)
                        counts[index] += count

                                                            # output stats
    for index, country in enumerate(countrys):
        print(f'Country: {country}, сумма по count: {counts[index]}, число уникальных user_id для country: {len(user_id[index])}')

                    
            

