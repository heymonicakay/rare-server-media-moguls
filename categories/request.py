import sqlite3
import json
from models import Category

def get_all_categories():
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.category
        FROM Category c
        """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:
                category = Category(row['id'], row['category'])

                categories.append(category.__dict__)

    return json.dumps(categories)

def create_category(new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Category
            ( category )
        VALUES
            ( ? );
        """, (new_category['category'],))

        id = db_cursor.lastrowid

        new_category['id'] = id

    return json.dumps(new_category)