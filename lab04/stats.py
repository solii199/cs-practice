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