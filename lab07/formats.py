import json


def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []

    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if not lines:
        return []

    headers_line, *data_lines = lines
    headers = [h.strip() for h in headers_line.split(',')]

    records = []
    for line in data_lines:
        values = [v.strip() for v in line.split(',')]
        record = {}
        for header, val in zip(headers, values):
            record[header] = val
        for header in headers:
            if header not in record:
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
        if '.' in val_str:
            return float(val_str)
        return int(val_str)
    except ValueError:
        return val_str


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None

    for line in lines:
        line_clean, *discard = line.split('#')
        line_clean = line_clean.rstrip()
        if not line_clean.strip():
            continue

        if line_clean.strip().startswith('-'):
            if current_list_key is not None:
                _, item_value = line_clean.strip().split('-', 1)
                item_value = item_value.strip()
                result[current_list_key].append(_convert_type(item_value))
            continue

        if ':' in line_clean:
            key, value = line_clean.split(':', 1)
            key = key.strip()
            value = value.strip()

            if value == '':
                current_list_key = key
                result[current_list_key] = []
            else:
                current_list_key = None
                result[key] = _convert_type(value)

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    updated_rows = []

    for row in rows:
        new_row = row.copy()
        match_value = str(new_row.get(key, ''))

        if match_value in extra:
            extra_data = extra[match_value]
            for k, v in extra_data.items():
                if k not in new_row:
                    new_row[k] = v

        updated_rows.append(new_row)

    return updated_rows


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, sort_keys=True, indent=2, ensure_ascii=False)
