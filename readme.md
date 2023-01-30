
# About the software

This is a program that reads CSV files and interprets them in SQL, that is, from the CSV file it creates a database that can be manipulated with SQLite commands.

## Prerequisites

1) Install Python 3.x
2) Install the Python csv module
3) Have SQLite3 installed


## to rotate

To run the program in Python and see the entire database, just run it in the terminal

```bash
   python3 script.py
```

To execute in SQLite and be able to handle it and have more visualization options, execute it in the terminal

```bash
   sqlite3 social.db
```
```sql
   sqlite> .import filename.csv tablename
```

In our case we will put

```sql
sqlite> .import social.csv social
```
To see the contents of the table, run

```sql
sqlite> .shema
```

Repeat this process for each of the three CSV files. You will then be able to view the created tables with the following command:

```sql
sqlite> SELECT * FROM table_name;
```