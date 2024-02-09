from Functions.get_user_input import user_input


def main() -> None:
    try:
        name: str = str(input('Enter your name: '))
        month: int = int(input('Enter your month of birth: '))
        year: int = int(input('Enter your year of birth: '))
    except ValueError:
        print("Incorrect data type")
    else:
        user_input(name=name, month=month, year=year)


if __name__ == '__main__':
    main()
