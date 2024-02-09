from Functions import validate_month, validate_year, validate_year_of_birth


def create_test_file(name: str, month: int, year: int) -> str:
    with open('test.txt', 'w') as file:
        file.write(
            f'Name: {name} \n'
            f'Age: {validate_year(month, year)}'
            f'Month of birth: {validate_month(month)}'
            f'Year of birth: {validate_year_of_birth(month, year)}'
        )
    return "Test file created successfully"
