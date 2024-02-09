from datetime import datetime


def validate_month(month: int) -> str:
    if month > 0 and month <= 12:
        date_string = month
        # Перетворюємо рядок у об'єкт datetime
        date_object = datetime.strptime(str(date_string), '%m')
        valide_month = date_object.strftime('%B')
        return valide_month
    else:
        return "The month is invalid"
