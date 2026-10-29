import json
import copy


def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []

    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(',')]

    records = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(',')]
        record = {}
        for i, header in enumerate(headers):
            if i < len(values):
                record[header] = values[i]
            else:
                record[header] = ""
        records.append(record)

    return records


def _convert_type(val_str: str):
    val_str = val_str.strip()


    if val_str.lower() in ('true', 'yes'):
        return True
    if val_str.lower() in ('false', 'no'):
        return False


    try:
        return int(val_str)
    except ValueError:
        pass

    try:
        return float(val_str.replace(',', '.'))
    except ValueError:
        pass

    return val_str






