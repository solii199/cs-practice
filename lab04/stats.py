def parse_record(line: str) -> dict:
    if len(line.split(';')) != 3:
        raise ValueError('полей не ровно 3: ')
    city, temp, date = line.split(';')
    if city == '' or date == '':
        raise ValueError('город или дата пустая: ')
    temp = float(temp)
    data = {'city': city, 'temp': temp, 'date': date}
    return data

def read_valid(lines: list[str]) -> list[dict]:
    valid = []
    for line in lines:
        try:
            data = parse_record(line)
            valid.append(data)
        except ValueError:
            pass
    return valid

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    temps = {}
    for record in records:
        city, temp, date = record.values()
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
    for city in total:
        temps[city] =  f"{total[city] / count[city]}"