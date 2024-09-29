Beispieldatenbank:

Chinook_Sqlite_AutoIncrementPKs.sqlite
Aufgaben:

Ansprechen der lokalen sqlite Datenbank

Skript, das einen Export der Tabelle "Customer" in ein CSV Format mit Trenner ";" erzeugt ^^ sind einfach

Skript, dem man Parameter übergeben muss für Tabellenname und diese dann in ein CSV mit Trenner "," exportiert ** Beispielaufruf: python3 export_table.py --table Album

Skript, das eine Ausgabe der Genre absteigend sortiert nach Anzahl der Track in dem Genre, mit Angabe der Anzahl erzeugt

Skript, das ein Excel File erzeugt mit: Auflistung der Kundennamen mit Rechnungssummen pro Jahr

Skript mit Übergabeparameter für ein Suchwort ** -> Exceldatei mit einem Tab pro Album, in dem das Suchwort vorkommt. ** Tab benamt nach Album (u.U. gekürzt) ** Je Sheet : Liste der Songtitel mit Künstler, MediaType Name, Genrename

Darstellung der transitiven "ReportsTo" - Relation (mit Nachname und Titel) in irgendeiner Form z.b. grafisch oder einfach als ASCII Ausgabe Beispiel:

Adams (General Manager) |\Edwards (Sales Manager) ||\Peacock (Sales Support Agent) ||\Park (Sales Support Agent) ||\Johnson (Sales Support Agent) |\Mitchell (IT Manager) ||\King (IT Staff) ||\Callahan (IT Staff)

Anlaufstellung für Hilfe:

SQLite Datenbank: ** Datenbank Diagramm: https://cdn.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf ** https://pymotw.com/3/sqlite3/ ** https://sqlitebrowser.org/
CSV ** https://pymotw.com/3/csv/
Python Skripte mit Übergabeparameter: ** https://pymotw.com/3/argparse/
Excel ** https://openpyxl.readthedocs.io/en/stable/ ** https://xlsxwriter.readthedocs.io/
Generelle einsteigerfreundliche Infos ** https://automatetheboringstuff.com/