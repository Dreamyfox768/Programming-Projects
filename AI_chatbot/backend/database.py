import sqlite3
from datetime import date


class Database:
    """
    Handles all database operations for storing and retrieving mood data.
    Uses a SQLite database with a single table: moods.
    """

    def __init__(self, db_path="mood.db"):
        """
        Initializes the database handler.
        Ensures the required table exists.
        """
        self.db_path = db_path
        self.create_table()

    def connect(self):
        """
        Opens and returns a database connection.
        """
        return sqlite3.connect(self.db_path)

    def create_table(self):
        """
        Creates the 'moods' table if it does not already exist.
        The table stores:
            id    -> auto-incrementing primary key
            date  -> YYYY-MM-DD as text
            moods -> comma-separated mood labels
        """
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
        """
        Inserts a new mood entry into the database.
        The 'moods' list is stored as a comma-separated string.
        """
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO moods (date, moods) VALUES (?, ?)",
            (str(date), ",".join(moods))
        )

        conn.commit()
        conn.close()

    def get_moods_last_10_days(self):
        """
        Retrieves all mood entries from the last 10 days.
        Returns a list of dictionaries, each containing:
            { "date": "YYYY-MM-DD", "moods": [list of mood labels] }
        """
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
