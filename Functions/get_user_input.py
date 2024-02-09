from Functions import validate_month, validate_year, validate_year_of_birth, create_test_file


def user_input(name: str, month: int, year: int) -> None:
    print(
        f"Name: {name}\n"
        f"Age: {validate_year(month, year)}\n"
        f"Month of birth: {validate_month(month)}\n"
        f"Year of birth: {validate_year_of_birth(month, year)}\n"
        f"{create_test_file(name, month, year)}\n"
    )
