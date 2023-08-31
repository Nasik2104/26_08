# Створити нову таблицю з полями id_subject, subject_name, subject_description, hours, semester_number; 
# заповнитити її даними (мінімум 8 записів); прочитати дані з колонок subject_name, semester_number.

import sqlite3

with sqlite3.connect('study.db') as db:
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study(
        id_subject INTEGER,
        subject_name VARCHAR(255),
        subject_description VARCHAR(255),
        hours NUMERIC,
        semester_number NUMERIC
    )
    """)
    
    cursor.execute("""
    INSERT INTO study VALUES
        (1, "History", "this subject is studying history", 3, 1),
        (2, "Geography", "this subject is studying Earth", 2, 1),
        (3, "Ukrainian", "this subject is studying Ukrainian language", 3, 1),
        (4, "Ukrainian literature", "this subject is studying Ukrainian literature", 2, 1),
        (5, "Math", "This is the horseman of the apocalypse", 3, 1),
        (6, "Chemistry", "May be. Approved", 2, 1),
        (7, "Physics", "It's beautiful", 2, 1),
        (8, "Biology", "It's a piece of dog shit", 2, 1)
    """)
    
    cursor.execute("""
        SELECT subject_name, semester_number 
        FROM study
    """)
    result = cursor.fetchall()
    for row in result:
        print(row)