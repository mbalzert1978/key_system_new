from sqlite_repo import SqliteRepository


def main():
    repo = SqliteRepository("Chinook_Sqlite_AutoIncrementPKs.sqlite")
    print(repo.show_tables())


if __name__ == "__main__":
    main()
