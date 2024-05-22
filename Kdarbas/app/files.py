from schemas import BirthdayRead
import json


class FileOperator:
    def save_birthdays_to_file(birthdays: list[BirthdayRead], filename: str):
        with open(filename, 'w') as file:
            json.dump([birthday.model_dump() for birthday in birthdays], file)

    def load_birthdays_from_file(filename: str) -> list[BirthdayRead]:
        with open(filename, 'r') as file:
            data = json.load(file)
        return [BirthdayRead(**birthday) for birthday in data]


filename = "birthdays.txt"
