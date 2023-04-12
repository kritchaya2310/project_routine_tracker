import sqlite3


def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS routine")
    cur.execute("CREATE TABLE routine (Id INTEGER PRIMARY KEY , date text , earnings integer , exercise text , study text , diet text , expense integer)")
    conn.commit()
    conn.close()


def insert(date, earnings, exercise, study, diet, expense):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)",
                (date, earnings, exercise, study, diet, expense))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?",
                (id,))
    conn.commit()
    conn.close()


def search(date='', earnings='', exercise='', study='', diet='', expense=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earnings=? OR exercise=? OR study=? OR diet=? OR expense=? ",
                (date, earnings, exercise, study, diet, expense))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    print("Number of rows returned: ", len(rows))
    return rows


def edit(id, date='', earnings='', exercise='', study='', diet='', expense=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("UPDATE routine SET date=?, earnings=?, exercise=?, study=?, diet=?, expense=? WHERE id=?",
                (date, earnings, exercise, study, diet, expense, id))
    conn.commit()
    conn.close()
