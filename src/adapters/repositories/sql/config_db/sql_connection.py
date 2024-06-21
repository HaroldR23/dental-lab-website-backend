import os


class SQLConnection():
    def get_connection_string(self) -> str:
        return f"{os.environ.get('SQL_URL')}"
