import sys
from logstats import count_levels, top_errors, format_report

def main():
    file_name = sys.stdin.readline().strip()
    if not file_name:
        return

    # Делаем два прохода, чтобы не перегружать память
    with open(file_name, "r", encoding="utf-8") as log:
        counts = count_levels(log)

    with open(file_name, "r", encoding="utf-8") as log:
        errors = top_errors(log, 3)

    total_parsed = sum(counts.values())
    print(f"{total_parsed} {counts['ERROR']} {counts['BROKEN']}")

    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)

if __name__ == "__main__":
    main()
