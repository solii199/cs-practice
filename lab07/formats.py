import json


def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []
    lines = []
    for line in text.split('\n'):
        if line.strip():
            lines.append(line.strip())
    if not lines:
        return []

    headers_line = ""
    for line in lines:
        headers_line = line
        break

    headers = []
    for h in headers_line.split(','):
        headers.append(h.strip())

    records = []
    skip = True
    for line in lines:
        if skip:
            skip = False
            continue
        values = []
        for v in line.split(','):
            values.append(v.strip())
        record = {}
        for i in range(len(headers)):
            header = headers[i]
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
    if ',' in val_str:
        return val_str
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
        line_clean = ""
        for part in line.split('#'):
            line_clean = part
            break

        if not line_clean.strip():
            continue

        if line_clean.strip().startswith('-'):
            if current_list_key is not None:
                content = line_clean.strip()
                item_value = content[1:].strip()
                result[current_list_key].append(_convert_type(item_value))
            continue

        if ':' in line_clean:
            parts = line_clean.split(':', 1)
            key = ""
            value = ""
            is_key = True
            for p in parts:
                if is_key:
                    key = p.strip()
                    is_key = False
                else:
                    value = p.strip()
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
