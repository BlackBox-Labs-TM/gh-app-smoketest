# human af

import sys

def parse_input(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise ValueError("Line must contain name,subject,grade")
    name, subject, grade = parts
    return name.strip(), subject.strip(), float(grade.strip())

def average_grade(records, subject=None):
    total = 0
    count = 0
    for r in records:
        if subject and r[1] != subject:
            continue
        total += r[2]
        count += 1
    return total / count if count > 0 else 0

def main():
    print("Grade Manager CLI (Ctrl+D to end)")
    data = []
    for line in sys.stdin:
        try:
            entry = parse_input(line)
            data.append(entry)
        except Exception as e:
            print(f"Error: {e}")
    print("--- Summary ---")
    subjects = {r[1] for r in data}
    for s in subjects:
        avg = average_grade(data, s)
        print(f"{s}: {avg:.2f}")
    overall = average_grade(data)
    print(f"Overall average: {overall:.2f}")

if __name__ == "__main__":
    main()

