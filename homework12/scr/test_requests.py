import requests
import json

BASE_URL = 'http://127.0.0.1:5000'
OUTPUT_FILE = 'results.txt'

# Функція для виводу в консоль та запису у файл одночасно
def log(message):
    print(message)
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

def run_tests():
    # Очищуємо файл результатів перед запуском
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("--- REST API TEST RESULTS ---\n")

    log("\n1. ОТРИМАТИ ВСІХ НАЯВНИХ СТУДЕНТІВ (GET)")
    try:
        response = requests.get(f'{BASE_URL}/students')
        log(f"Status: {response.status_code}")
        log(f"Response: {response.json()}")
    except requests.exceptions.ConnectionError:
        log("ПОМИЛКА: Сервер не запущено. Запустіть app.py!")
        return

    log("\n2. СТВОРИТИ ТРЬОХ СТУДЕНТІВ (POST)")
    students_data = [
        {"first_name": "Ivan", "last_name": "Petrov", "age": "20"},
        {"first_name": "Maria", "last_name": "Ivanova", "age": "22"},
        {"first_name": "Oleg", "last_name": "Sidorov", "age": "25"}
    ]
    
    created_ids = []
    
    for student in students_data:
        response = requests.post(f'{BASE_URL}/students', json=student)
        log(f"Creating {student['first_name']}... Status: {response.status_code}")
        log(f"Response: {response.json()}")
        if response.status_code == 201:
            created_ids.append(response.json()['id'])

    log("\n3. ОТРИМАТИ ІНФОРМАЦІЮ ПРО ВСІХ (GET)")
    response = requests.get(f'{BASE_URL}/students')
    log(f"Status: {response.status_code}")
    log(f"Response: {json.dumps(response.json(), indent=2)}")

    if len(created_ids) >= 2:
        student_2_id = created_ids[1] # Другий студент
        
        log(f"\n4. ОНОВИТИ ВІК ДРУГОГО СТУДЕНТА (PATCH ID: {student_2_id})")
        patch_data = {"age": "30"}
        response = requests.patch(f'{BASE_URL}/students/{student_2_id}', json=patch_data)
        log(f"Status: {response.status_code}")
        log(f"Response: {response.json()}")

        log(f"\n5. ОТРИМАТИ ІНФОРМАЦІЮ ПРО ДРУГОГО СТУДЕНТА (GET ID: {student_2_id})")
        response = requests.get(f'{BASE_URL}/students/{student_2_id}')
        log(f"Status: {response.status_code}")
        log(f"Response: {response.json()}")

    if len(created_ids) >= 3:
        student_3_id = created_ids[2] # Третій студент

        log(f"\n6. ОНОВИТИ ВСЕ ДЛЯ ТРЕТЬОГО СТУДЕНТА (PUT ID: {student_3_id})")
        put_data = {"first_name": "Oleg_Updated", "last_name": "Sidorov_Updated", "age": "99"}
        response = requests.put(f'{BASE_URL}/students/{student_3_id}', json=put_data)
        log(f"Status: {response.status_code}")
        log(f"Response: {response.json()}")

        log(f"\n7. ОТРИМАТИ ІНФОРМАЦІЮ ПРО ТРЕТЬОГО СТУДЕНТА (GET ID: {student_3_id})")
        response = requests.get(f'{BASE_URL}/students/{student_3_id}')
        log(f"Status: {response.status_code}")
        log(f"Response: {response.json()}")

    log("\n8. ОТРИМАТИ ВСІХ НАЯВНИХ СТУДЕНТІВ (GET)")
    response = requests.get(f'{BASE_URL}/students')
    log(f"Status: {response.status_code}")
    log(f"Response: {json.dumps(response.json(), indent=2)}")

    if len(created_ids) >= 1:
        student_1_id = created_ids[0] # Перший студент
        
        log(f"\n9. ВИДАЛИТИ ПЕРШОГО КОРИСТУВАЧА (DELETE ID: {student_1_id})")
        response = requests.delete(f'{BASE_URL}/students/{student_1_id}')
        log(f"Status: {response.status_code}")
        log(f"Response: {response.json()}")

    log("\n10. ОТРИМАТИ ВСІХ НАЯВНИХ СТУДЕНТІВ (GET)")
    response = requests.get(f'{BASE_URL}/students')
    log(f"Status: {response.status_code}")
    log(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    run_tests()
    print(f"\nТестування завершено. Результати збережено у {OUTPUT_FILE}")