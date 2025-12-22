from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = 'students.csv'
VALID_FIELDS = {'first_name', 'last_name', 'age'}

@app.route('/students', methods=['GET'])
def get_all_students():
    students = read_students()
    return jsonify(students), 200

def read_students():
    # Додано перевірку: якщо файлу немає, повертаємо порожній список, щоб не було помилки
    if not os.path.exists(CSV_FILE):
        return []
    
    students = []
    with open(CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    students = read_students()
    _, student = find_student_by_id(students, student_id)
    if student:
        return jsonify(student), 200
    
    return jsonify({'error': f'Student with id {student_id} not found'}), 404

def find_student_by_id(students, student_id):
    for index, student in enumerate(students):
        if student['id'] == str(student_id):
            return index, student
    return None, None

@app.route('/students/lastname/<last_name>', methods=['GET'])
def get_students_by_last_name(last_name):
    students = read_students()
    match_students = [
        student for student in students
        if student['last_name'].lower() == last_name.lower()
    ]
    # Прибрав print, щоб не засмічувати консоль, але можна залишити для дебагу
    # print(match_students) 
    if match_students:
        return jsonify(match_students), 200
    return jsonify({'error': f'No students were found with the lastname {last_name}'}), 404


def write_students(students):
    with open(CSV_FILE, 'w', newline='') as file:
        fieldnames = ['id', 'first_name', 'last_name', 'age']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def get_next_id(students):
    if not students:
        return 1
    return max(int(student['id']) for student in students) + 1


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No fields provided in the request body'}), 400
    
    provided_fields = set(data.keys())
    invalid_fields = provided_fields - VALID_FIELDS

    if invalid_fields:
        return jsonify({'error': f'Invalid fields provided in the request body: {sorted(list(invalid_fields))}'}), 400

    # Перевірка на обов'язкові поля при створенні (опціонально, але бажано)
    if not VALID_FIELDS.issubset(provided_fields):
         return jsonify({'error': f'Missing required fields: {VALID_FIELDS - provided_fields}'}), 400

    students = read_students()
    new_id = get_next_id(students)

    new_student = {
        'id': str(new_id),
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'age': str(data['age'])
    }

    students.append(new_student)
    write_students(students)

    return jsonify(new_student), 201

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    students = read_students()
    index, student = find_student_by_id(students, student_id)
    if student is None:
        return jsonify({'error': f'Student with id {student_id} not found'}), 404

    deleted_student = students.pop(index)
    write_students(students)

    return jsonify({'message': f"Student {deleted_student['first_name']} {deleted_student['last_name']} removed"}), 200

@app.route('/students/<int:student_id>', methods=['PATCH'])
def patch_student_age(student_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': "No fields provided in the request body"}), 400
    
    provided_fields = set(data.keys())
    allowed_patched_fields = {'age'}
    invalid_fields = provided_fields - allowed_patched_fields
    
    if invalid_fields:
        return jsonify({'error': f'Invalid fields in PATCH: {invalid_fields}. Only the age is allowed.'}), 400
    
    if 'age' not in data:
        return jsonify({'error': 'Age field is required in PATCH'}), 400

    try:
        age = int(data['age'])
    except (TypeError, ValueError):
        return jsonify({'error': 'Age must be an integer'}), 400

    students = read_students()
    index, student = find_student_by_id(students, student_id)
    
    if student is None:
        return jsonify({'error': f'Student with id {student_id} not found'}), 404

    students[index]['age'] = str(age)
    write_students(students)

    return jsonify(students[index]), 200

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No fields provided in the request body'}), 400

    provided_fields = set(data.keys())
    invalid_fields = provided_fields - VALID_FIELDS

    if invalid_fields:
        return jsonify({'error': f'Invalid fields in PUT: {invalid_fields}. Only {VALID_FIELDS} are allowed.'}), 400

    students = read_students()
    index, student = find_student_by_id(students, student_id)

    if student is None:
        return jsonify({'error': f'Student with id {student_id} is not found'}), 404

    for field in VALID_FIELDS:
        if field in data:
            students[index][field] = str(data[field])

    write_students(students)

    return jsonify(students[index]), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)