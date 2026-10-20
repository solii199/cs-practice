# logstats.py

VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:

    cleaned = line.strip()
    if not cleaned:
        raise ValueError("Пустая строка")

    parts = cleaned.split(None, 2)
    if len(parts) < 3:
        raise ValueError("Неверный формат строки (недостаточно элементов)")

    time, level, message = parts

    if level not in VALID_LEVELS:
        raise ValueError(f"Неизвестный или отсутствующий уровень: {level}")

    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}

    for line in lines:
        if not line or not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1

    return counts


def top_errors(lines, n: int) -> list[list]:
    error_counts = {}

    for line in lines:
        if not line or not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue

    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))

    return [list(item) for item in sorted_errors[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]

    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")

    lines.append("\nЧастые ошибки:")
    for msg, count in errors:
        lines.append(f"- {msg} — {count}")

    return "\n".join(lines) + "\n"

