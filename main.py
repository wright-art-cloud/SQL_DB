import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

# Reference code to view employee data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName 
FROM employees
""", conn)

df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber 
FROM employees
""", conn)

df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID 
FROM employees
""", conn)

df_executive = pd.read_sql("""
SELECT *,
    CASE 
        WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees
""", conn)

df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length 
FROM employees
""", conn)

df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
FROM employees
""", conn)

order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

sum_total_price = pd.read_sql("""
SELECT ROUND(SUM(priceEach * quantityOrdered), 0) AS total_amount 
FROM orderDetails
""", conn)

df_day_month_year = pd.read_sql("""
SELECT orderDate,
       STRFTIME('%d', orderDate) AS day,
       STRFTIME('%m', orderDate) AS month,
       STRFTIME('%Y', orderDate) AS year
FROM orders
""", conn)

conn.close()