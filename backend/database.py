import sqlite3

def init_db():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input TEXT,
        output TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_query(input_text, output_text):
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (input, output) VALUES (?, ?)",
        (input_text, output_text)
    )

    conn.commit()
    conn.close()