import sys

# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def __repr__(self):
        return f"Teacher({self.first_name} {self.last_name}, {self.age})"

def create_schedule(subjects, teachers):
    """
    Складає розклад занять за допомогою жадібного алгоритму.
    
    Аргументи:
        subjects (set): Множина всіх предметів, які потрібно покрити.
        teachers (list): Список об'єктів Teacher.
        
    Повертає:
        list: Список викладачів з призначеними предметами або None,
              якщо неможливо покрити всі предмети.
    """
    uncovered_subjects = set(subjects)
    schedule = []
    
    while uncovered_subjects:
        best_teacher = None
        subjects_covered_by_best = set()
        
        # Знаходимо найкращого викладача, який покриває найбільшу кількість
        # ще не охоплених предметів.
        for teacher in teachers:
            # Обчислюємо, скільки нових предметів цей викладач може покрити.
            newly_covered_subjects = teacher.can_teach_subjects.intersection(uncovered_subjects)
            
            # Використовуємо критерії жадібного алгоритму:
            # 1. Покриває найбільшу кількість предметів.
            # 2. Якщо кількість однакова, обираємо наймолодшого.
            if not best_teacher or \
               len(newly_covered_subjects) > len(subjects_covered_by_best) or \
               (len(newly_covered_subjects) == len(subjects_covered_by_best) and teacher.age < best_teacher.age):
                
                best_teacher = teacher
                subjects_covered_by_best = newly_covered_subjects
        
        # Якщо найкращий викладач не може покрити жодного нового предмета,
        # значить, розклад не може бути повністю складений.
        if not subjects_covered_by_best:
            return None
            
        # Призначаємо предмети знайденому викладачу і додаємо його до розкладу.
        best_teacher.assigned_subjects = subjects_covered_by_best
        schedule.append(best_teacher)
        
        # Оновлюємо множину непокритих предметів.
        uncovered_subjects -= subjects_covered_by_best
    
    return schedule

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"✔️ {teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("❌ Неможливо покрити всі предмети наявними викладачами.")