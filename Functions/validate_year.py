from datetime import datetime


def validate_year(month: int, year: int) -> int | str:
    current_year = datetime.now().year - year - (1 if datetime.now().month < month else 0)
    if current_year < 120 and current_year >= 5:
        return current_year
    else:
        return "The year is invalid"


def validate_year_of_birth(month: int, year: int) -> int | str:
    current_year = datetime.now().year - year - (1 if datetime.now().month < month else 0)
    if current_year < 120 and current_year >= 5:
        return year
    else:
        return "The year is invalid"
