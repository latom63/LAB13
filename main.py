import csv
import json

# -------------------- виконував Гетьман Ярослав --------------------
# Створення .csv файлу та конвертація його у .json

def create_csv(file_path):
    data = [
        {"id": 1, "name": "John Doe", "age": 25},
        {"id": 2, "name": "Jane Smith", "age": 30},
        {"id": 3, "name": "Bob Johnson", "age": 22}
    ]
    try:
        # Запис даних у CSV
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "age"])
            writer.writeheader()
            writer.writerows(data)
        print(f"СТУДЕНТ 1: CSV файл створено: {file_path}")
    except Exception as e:
        print(f"СТУДЕНТ 1: Помилка під час створення CSV файлу: {e}")

def csv_to_json(csv_file, json_file):
    try:
        # Читання з CSV
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        # Запис у JSON
        with open(json_file, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"СТУДЕНТ 1: Дані з CSV записано у JSON файл: {json_file}")
    except Exception as e:
        print(f"СТУДЕНТ 1: Помилка під час конвертації у JSON: {e}")

# -------------------- виконував Микитенко Мирослав --------------------
# Конвертація .json у .csv з додаванням нових рядків

def json_to_csv_with_additions(json_file, csv_file):
    try:
        # Зчитування JSON
        with open(json_file, mode='r', encoding='utf-8') as file:
            data = json.load(file)

        # Додавання нових записів
        additional_data = [
            {"id": 4, "name": "Alice Green", "age": 28},
            {"id": 5, "name": "Chris Blue", "age": 35}
        ]
        data.extend(additional_data)

        # Запис у CSV
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "age"])
            writer.writeheader()
            writer.writerows(data)
        print(f"СТУДЕНТ 2: Дані з JSON записано у CSV файл: {csv_file}")
    except Exception as e:
        print(f"СТУДЕНТ 2: Помилка під час роботи з файлами: {e}")

# -------------------- виконував Клiмов Теодор--------------------
# Конвертація оновленого .csv у .json з додаванням нових рядків

def csv_to_json_with_additions(csv_file, json_file):
    try:
        # Зчитування CSV
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        # Додавання нових записів
        additional_data = [
            {"id": 6, "name": "Eve White", "age": 26},
            {"id": 7, "name": "David Black", "age": 29}
        ]
        data.extend(additional_data)

        # Запис у JSON
        with open(json_file, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"СТУДЕНТ 3: Дані з CSV записано у JSON файл: {json_file}")
    except Exception as e:
        print(f"СТУДЕНТ 3: Помилка під час роботи з файлами: {e}")

# -------------------- ОСНОВНИЙ КОД --------------------

# гетьман
csv_file_1 = "students_data.csv"
json_file_1 = "students_data.json"
create_csv(csv_file_1)
csv_to_json(csv_file_1, json_file_1)

#микитенко
csv_file_2 = "updated_students_data.csv"
json_to_csv_with_additions(json_file_1, csv_file_2)

# клiмов
json_file_2 = "final_students_data.json"
csv_to_json_with_additions(csv_file_2, json_file_2)
