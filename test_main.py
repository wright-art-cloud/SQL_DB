import sqlite3
import pandas as pd

# ==========================================
# PART 1: Connecting to the Data
# ==========================================

# STEP 1A & 1B: Connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference code to view employee data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# ==========================================
# PART 2: Basic Select Filtering
# ==========================================

# STEP 2: Employee number and last name
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName 
FROM employees
""", conn)


# STEP 3: Last name come before employee number
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber 
FROM employees
""", conn)


# ==========================================
# PART 3: Aliasing in Select
# ==========================================

# STEP 4: Last name, and employee number aliased as 'ID'
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID 
FROM employees
""", conn)


# ==========================================
# PART 4: CASE Function
# ==========================================

# STEP 5: Bin jobTitles into 'Executive' or 'Not Executive'
df_executive = pd.read_sql("""
SELECT *,
    CASE 
        WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees
""", conn)


# ==========================================
# PART 5: Built-In Functions - Strings
# ==========================================

# STEP 6: Length of the last name for all employees as 'name_length'
df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length 
FROM employees
""", conn)


# STEP 7: First two letters of each person's job title as 'short_title'
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
FROM employees
""", conn)


# ==========================================
# PART 6: Built-In Functions - Numerics & Dates
# ==========================================

# Reference code to view order details data
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8: Total amount for all orders (sum of rounded total prices)
sum_total_price = pd.read_sql("""
SELECT SUM(ROUND(priceEach * quantityOrdered, 2)) AS total_amount 
FROM orderDetails
""", conn).sum()


# STEP 9: Return original order date, followed by 'day', 'month', and 'year' columns
df_day_month_year = pd.read_sql("""
SELECT orderDate,
       STRFTIME('%d', orderDate) AS day,
       STRFTIME('%m', orderDate) AS month,
       STRFTIME('%Y', orderDate) AS year
FROM orderDetails
""", conn)


# ==========================================
# Close Connection
# ==========================================
conn.close()