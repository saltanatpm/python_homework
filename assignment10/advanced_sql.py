import sqlite3

def main():
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()

    # TASK 1: ORDER TOTALS
    sql_task1 = """
    SELECT
        li.order_id,
        SUM(p.price * li.quantity) AS total_price
    FROM line_items li
    JOIN products p
        ON li.product_id = p.product_id
    GROUP BY li.order_id
    ORDER BY li.order_id
    LIMIT 5;
    """
    print("\nTASK 1: Order Totals\n")
    cursor.execute(sql_task1)
    for row in cursor.fetchall():
        print(row)


    # TASK 2: AVERAGE ORDER VALUE
    sql_task2 = """
    SELECT AVG(total_price)
    FROM (
        SELECT
            li.order_id,
            SUM(p.price * li.quantity) AS total_price
        FROM line_items li
        JOIN products p
            ON li.product_id = p.product_id
        GROUP BY li.order_id
    );
    """
    print("\nTASK 2: Average Order Price\n")
    cursor.execute(sql_task2)
    result = cursor.fetchone()
    print(result[0])


    # TASK 3: TRANSACTION INSERT
    print("\nTASK 3: Creating new order transaction\n")

    try:
        # 1. Get 5 cheapest products
        cursor.execute("""
            SELECT product_id
            FROM products
            ORDER BY price ASC
            LIMIT 5;
        """)
        product_ids = [row[0] for row in cursor.fetchall()]
        print("Cheapest products:", product_ids)

        # 2. Create new order_id
        cursor.execute("""
            SELECT IFNULL(MAX(order_id), 0) + 1
            FROM line_items;
        """)
        order_id = cursor.fetchone()[0]
        print("New order_id:", order_id)

        # 3. Insert line items
        for pid in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?);
            """, (order_id, pid, 10))

        conn.commit()
        cursor.execute("""
            SELECT
                li.line_item_id,
                li.quantity,
                p.product_name
            FROM line_items li
            JOIN products p
                ON li.product_id = p.product_id
            WHERE li.order_id = ?
            ORDER BY li.line_item_id;
        """, (order_id,))

        print("\nInserted Order Line Items:\n")
        for row in cursor.fetchall():
            print(row)

    except sqlite3.Error as e:
        conn.rollback()
        print("Transaction failed:", e)


    # TASK 4: HAVING CLAUSE
    print("\nTASK 4: Employees with More Than 5 Orders\n")

    sql_task4 = """
    SELECT
        e.employee_id,
        e.first_name,
        e.last_name,
        COUNT(o.order_id) AS order_count
    FROM employees e
    JOIN orders o
        ON e.employee_id = o.employee_id
    GROUP BY
        e.employee_id,
        e.first_name,
        e.last_name
    HAVING COUNT(o.order_id) > 5;
    """

    try:
        cursor.execute(sql_task4)
        rows = cursor.fetchall()

        if not rows:
            print("No employees found with more than 5 orders.")
        else:
            for row in rows:
                print(row)

    except sqlite3.Error as e:
        print("Task 4 Error:", e)

    conn.close()

if __name__ == "__main__":
    main()