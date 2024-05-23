import schemas as scheme
import json
from typing import List, Dict


class FileOperator:
    def save_birthdays_to_file(birthdays: List[scheme.BirthdayRead], filename: str):
        with open(filename, 'w') as file:
            birthday_dicts = [
                {
                    "id": birthday.id,
                    "user_id": birthday.user_id,
                    "Name": birthday.Name,
                    "Date": birthday.Date.isoformat()  # Convert date to ISO format string
                }
                for birthday in birthdays
            ]
            json.dump(birthday_dicts, file)

            
filename = "birthdays.json"
