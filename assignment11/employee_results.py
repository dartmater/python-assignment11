import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../db/lesson.db')
query = """
SELECT last_name, SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""
employee_results = pd.read_sql(query, conn)

employee_results.plot.bar(x='last_name', y='revenue', color='skyblue')
plt.title('Employee Revenue')
plt.xlabel('Last Name')
plt.ylabel('Revenue ($)')
plt.show()
conn.close()