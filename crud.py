import os
import mysql.connector

def create_employee(empname,department,salary):
    """Creates a new employee in the database."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="employee_db"
    )
    cursor=connection.cursor()
    cursor.execute("INSERT INTO tblemployee (empname, department, salary) VALUES (%s, %s, %s)",(empname, department, salary))
    connection.coomit()
    cursor.close()

def read_employees():
    """Returns a list of all employees in the database."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="employee_db"
    )
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM tblemployee")
    employees = cursor.fetchall()
    cursor.close()
    return employees

def update_employee(empid, empname, department, salary):
    """Updates the employee with the given ID in the database"""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="employee_db"
    )
    cursor=connection.cursor()
    cursor.execute("UPDATE tblemployee SET empname=%s, department=%s, salary=%s WHERE empid=%s", (empname, department, salary, empid))
    connection.commit()
    cursor.close()

def delete_employee(empid):
    """Deletes the employee with the given ID from the database."""
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="employee_db"
    )
    cursor=connection.cursor()
    cursor.execute("DELETE FROM tblemployee WHERE empid=%s",(empid,))
    connection.commit()
    cursor.close()

if __name__=="__main__":
    create_employee("Arushi Verma","Engineering",30000)
    employees=read_employees()
    for employee in employees:
        print(employee)
    update_employee(1,"Arushi Verma","HR",20000)
    employees=read_employees()
    for employee in employees:
        print(employee)
    delete_employee(1)
    employees=read_employees()
    print(employees)


