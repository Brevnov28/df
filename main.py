from datetime import datetime, date, time
from application.salary import calculate_salary


def main():
    time = datetime.now()
    print(time)

    print(calculate_salary())


if __name__ == '__main__':
    main()