def parse_record(line: str) -> dict:
    if len(line.split(';')) != 3:
        raise ValueError('полей не ровно 3: ')

    city, temp, date = line.split(';')

    city = city.strip()
    temp = temp.strip()
    date = date.strip()

    if city == '' or date == '':
        raise ValueError('город или дата пустая: ')

    try:
        temp = float(temp)
    except ValueError:
        raise ValueError('Температура должна быть числом: ')

    data = {'city': city, 'temp': temp, 'date': date}
    return data

def read_valid(lines: list[str]) -> list[dict]:
    valid = []
    for line in lines:
        if not line.strip():
            continue
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
        temps[city] = round(total[city] / count[city], 1)
    return temps

def warmest_city(records: list[dict]) -> str:
    temps = average_by_city(records)
    best = ''
    for city in temps:
        if best == '' or temps[city] > temps[best] or (temps[city] == temps[best] and city < best):
            best = city
        return best


