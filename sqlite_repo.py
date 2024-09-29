import operator
import sqlite3
from os import PathLike

from abstraction.repo import Id

GET_TABLES = """
    SELECT
        name
    FROM
        sqlite_master
    WHERE
        type ='table' 
    AND
        name
    NOT LIKE 
        'sqlite_%';
"""


class SqliteRepository:
    def __init__(self, db_path: PathLike):
        self.db_path = db_path

    def show_tables(self) -> tuple[str]:
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.cursor().execute(GET_TABLES).fetchall()
            return tuple(map(operator.itemgetter(0), rows))

    def read(self, id: Id) -> object: ...
