import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute(
            "SELECT * FROM publishers WHERE name = ?",
            (name,)
        )
        if cursor.fetchone():
            print(f"Publisher '{name}' already exists.")
            return
        cursor.execute(
            "INSERT INTO publishers (name) VALUES (?)",
            (name,)
        )

    except sqlite3.Error as e:
        print("Publisher Error:", e)

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute(
            "SELECT * FROM magazines WHERE name = ?",
            (name,)
        )

        if cursor.fetchone():
            print(f"Magazine '{name}' already exists.")
            return

        cursor.execute(
            """
            INSERT INTO magazines
            (name, publisher_id)
            VALUES (?, ?)
            """,
            (name, publisher_id)
        )

    except sqlite3.Error as e:
        print("Magazine Error:", e)

def add_subscriber(cursor, name, address):
    try:
        cursor.execute(
            """
            SELECT *
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (name, address)
        )

        if cursor.fetchone():
            print(f"Subscriber '{name}' already exists.")
            return
        cursor.execute(
            """
            INSERT INTO subscribers
            (name, address)
            VALUES (?, ?)
            """,
            (name, address)
        )

    except sqlite3.Error as e:
        print("Subscriber Error:", e)

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute(
            """
            SELECT *
            FROM subscriptions
            WHERE subscriber_id = ?
            AND magazine_id = ?
            """,
            (subscriber_id, magazine_id)
        )
        if cursor.fetchone():
            print(
                f"Subscription already exists for "
                f"subscriber {subscriber_id} "
                f"and magazine {magazine_id}."
            )
            return
        cursor.execute(
            """
            INSERT INTO subscriptions
            (
                subscriber_id,
                magazine_id,
                expiration_date
            )
            VALUES (?, ?, ?)
            """,
            (
                subscriber_id,
                magazine_id,
                expiration_date
            )
        )
    except sqlite3.Error as e:
        print("Subscription Error:", e)
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Connected to database.")
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        
# Create Tables
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
            """)
        except sqlite3.Error as e:
            print(e)

        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id)
                REFERENCES publishers(publisher_id)
            )
            """)
        except sqlite3.Error as e:
            print(e)

        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
            """)
        except sqlite3.Error as e:
            print(e)

        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id)
                REFERENCES subscribers(subscriber_id),
                FOREIGN KEY (magazine_id)
                REFERENCES magazines(magazine_id)
            )
            """)
        except sqlite3.Error as e:
            print(e)

# Populate Tables

        add_publisher(cursor, "Time Inc")
        add_publisher(cursor, "National Geographic")
        add_publisher(cursor, "Conde Nast")

        add_magazine(cursor, "TIME", 1)
        add_magazine(cursor, "National Geographic Magazine", 2)
        add_magazine(cursor, "Vogue", 3)

        add_subscriber(
            cursor,
            "Alice Smith",
            "123 Main Street"
        )

        add_subscriber(
            cursor,
            "Bob Jones",
            "456 Oak Avenue"
        )

        add_subscriber(
            cursor,
            "Carol White",
            "789 Pine Road"
        )

        add_subscription(
            cursor,
            1,
            1,
            "2026-12-31"
        )

        add_subscription(
            cursor,
            1,
            2,
            "2026-10-15"
        )

        add_subscription(
            cursor,
            2,
            3,
            "2027-01-01"
        )

        conn.commit()

        print("\nData inserted successfully.")
# Query 1
        print("\nALL SUBSCRIBERS")

        try:
            cursor.execute(
                "SELECT * FROM subscribers"
            )

            for row in cursor.fetchall():
                print(row)
        except sqlite3.Error as e:
            print(e)
# Query 2
        print("\nMAGAZINES SORTED BY NAME")
        try:
            cursor.execute("""
            SELECT *
            FROM magazines
            ORDER BY name
            """)
            for row in cursor.fetchall():
                print(row)

        except sqlite3.Error as e:
            print(e)
# Query 3
        print("\nMAGAZINES FOR TIME INC")

        try:
            cursor.execute("""
            SELECT m.name, p.name
            FROM magazines m
            JOIN publishers p
            ON m.publisher_id = p.publisher_id
            WHERE p.name = 'Time Inc'
            """)
            for row in cursor.fetchall():
                print(row)
        except sqlite3.Error as e:
            print(e)

except sqlite3.Error as e:
    print("Database Error:", e)