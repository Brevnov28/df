from .db.people import get_employees

def calculate_salary():
    print(get_employees())

    return 'You are in calculate_salary function'