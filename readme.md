
# About the software

This is a program that reads CSV files and interprets them in SQL, that is, from the CSV file it creates a database that can be manipulated with SQLite commands.

## Loke my movie in YouTube


<a href="https://www.youtube.com/watch?v=yfqjQO0GAg0&t=662s">
</a>
    <img src="./imgs/miniatura.png" alt="Miniatura-You-Tube-dinheiro-em-casa-dicas-gra-tis" border="0">
    <img>



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

<br>

<div>
        
   <a href="https://www.instagram.com/devbrunoo/" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
    <a href="https://medium.com/@devbrunoo" target="_blank"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" target="_blank"></a> 
    <a href="https://www.quora.com/profile/DevBrunoo" target="_blank"><img src="https://img.shields.io/badge/Quora-%23B92B27.svg?&style=for-the-badge&logo=Quora&logoColor=white" target="_blank"></a>
   <a href="https://codepen.io/brunobyhow15" target="_blank"><img src="https://img.shields.io/badge/Codepen-000000?style=for-the-badge&logo=codepen&logoColor=white" target="_blank"></a> 
    <a href = "mailto:contactbruno5@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    <a href="https://www.linkedin.com/in/devbruono/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
  
   
  </div>

<div>
<br>
<hr>
  <br>
</div>