# core/database.py
import sqlite3
from datetime import date

class Database:
    def __init__(self, db_path="mood.db"):
        self.db_path = db_path
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS moods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                moods TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def add_mood(self, date: date, moods: list):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO moods (date, moods) VALUES (?, ?)",
            (str(date), ",".join(moods))
        )

        conn.commit()
        conn.close()

    def get_moods_last_10_days(self):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT date, moods
            FROM moods
            WHERE date >= date('now', '-10 days')
            ORDER BY date ASC
        """)

        rows = cur.fetchall()
        conn.close()

        data = []
        for row in rows:
            data.append({
                "date": row[0],
                "moods": row[1].split(",") if row[1] else []
            })
        return data
