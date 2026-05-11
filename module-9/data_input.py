import mysql.connector
from mysql.connector import Error


def connect_to_database():
    """Connect to the MySQL database."""
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="your_database_name"
        )

        if db.is_connected():
            print("Connected to the database successfully.")
            return db

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def insert_advisors(cursor):
    """Insert 6 advisor records."""

    advisors = [
        (1, "Sarah", "Johnson", "CFP", "sarah.johnson@email.com", "402-555-1001"),
        (2, "Michael", "Smith", "CPA", "michael.smith@email.com", "402-555-1002"),
        (3, "Emily", "Davis", "CFA", "emily.davis@email.com", "402-555-1003"),
        (4, "David", "Brown", "CFP", "david.brown@email.com", "402-555-1004"),
        (5, "Jessica", "Wilson", "MBA", "jessica.wilson@email.com", "402-555-1005"),
        (6, "Robert", "Miller", "CFA", "robert.miller@email.com", "402-555-1006")
    ]

    sql = """
        INSERT INTO ADVISOR 
        (advisor_id, first_name, last_name, credentials, email, phone)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(sql, advisors)


def insert_clients(cursor):
    """Insert 6 client records."""

    clients = [
        (1, "John", "Anderson", "john.anderson@email.com", "402-555-2001", "2024-01-15", 1),
        (2, "Amanda", "Taylor", "amanda.taylor@email.com", "402-555-2002", "2024-02-20", 2),
        (3, "Chris", "Martin", "chris.martin@email.com", "402-555-2003", "2024-03-10", 3),
        (4, "Olivia", "White", "olivia.white@email.com", "402-555-2004", "2024-04-05", 4),
        (5, "Daniel", "Thomas", "daniel.thomas@email.com", "402-555-2005", "2024-05-18", 5),
        (6, "Sophia", "Moore", "sophia.moore@email.com", "402-555-2006", "2024-06-22", 6)
    ]

    sql = """
        INSERT INTO CLIENT
        (client_id, first_name, last_name, email, phone, enrollment_date, advisor_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(sql, clients)


def insert_accounts(cursor):
    """Insert 6 account records."""

    accounts = [
        (1, 1, "Checking", 2500.00, "USD", "2024-01-20"),
        (2, 2, "Savings", 8500.50, "USD", "2024-02-25"),
        (3, 3, "Investment", 15000.75, "USD", "2024-03-15"),
        (4, 4, "Retirement", 32000.00, "USD", "2024-04-10"),
        (5, 5, "Checking", 1200.25, "USD", "2024-05-22"),
        (6, 6, "Savings", 10450.80, "USD", "2024-06-30")
    ]

    sql = """
        INSERT INTO ACCOUNT
        (account_id, client_id, account_type, balance, currency, open_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(sql, accounts)


def insert_transactions(cursor):
    """Insert 6 transaction records."""

    transactions = [
        (1, 1, "2024-02-01", "Deposit", 500.00, "Initial account deposit"),
        (2, 2, "2024-03-05", "Deposit", 1200.00, "Monthly savings deposit"),
        (3, 3, "2024-04-12", "Withdrawal", 750.00, "Investment withdrawal"),
        (4, 4, "2024-05-03", "Deposit", 2000.00, "Retirement contribution"),
        (5, 5, "2024-06-14", "Withdrawal", 200.00, "ATM withdrawal"),
        (6, 6, "2024-07-01", "Deposit", 950.00, "Paycheck deposit")
    ]

    sql = """
        INSERT INTO TRANSACTION
        (transaction_id, account_id, transaction_date, transaction_type, amount, description)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(sql, transactions)


def insert_appointments(cursor):
    """Insert 6 appointment records."""

    appointments = [
        (1, 1, 1, "2024-02-10", "09:00:00", "Initial financial planning meeting"),
        (2, 2, 2, "2024-03-12", "10:30:00", "Review savings goals"),
        (3, 3, 3, "2024-04-18", "13:00:00", "Discuss investment strategy"),
        (4, 4, 4, "2024-05-20", "14:15:00", "Retirement planning session"),
        (5, 5, 5, "2024-06-25", "11:00:00", "Account review meeting"),
        (6, 6, 6, "2024-07-08", "15:30:00", "Annual portfolio review")
    ]

    sql = """
        INSERT INTO APPOINTMENT
        (appointment_id, client_id, advisor_id, appt_date, appt_time, notes)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(sql, appointments)


def insert_compliance_records(cursor):
    """Insert 6 compliance records."""

    compliance_records = [
        (1, "2024-02-15", "Account Review", "Passed", "Karen Lee"),
        (2, "2024-03-20", "Risk Assessment", "Passed", "Mark Allen"),
        (3, "2024-04-22", "Transaction Audit", "Needs Follow-Up", "Linda Harris"),
        (4, "2024-05-30", "Policy Review", "Passed", "James Young"),
        (5, "2024-06-18", "Client Documentation", "Passed", "Rachel King"),
        (6, "2024-07-12", "Security Review", "Needs Follow-Up", "Steven Wright")
    ]

    sql = """
        INSERT INTO COMPLIANCE_RECORD
        (compliance_id, review_date, review_type, outcome, reviewed_by)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.executemany(sql, compliance_records)


def insert_employees(cursor):
    """Insert 6 employee records."""

    employees = [
        (1, "Karen", "Lee", "Compliance Officer", "Full-Time", "karen.lee@email.com", "402-555-3001"),
        (2, "Mark", "Allen", "Auditor", "Full-Time", "mark.allen@email.com", "402-555-3002"),
        (3, "Linda", "Harris", "Risk Analyst", "Part-Time", "linda.harris@email.com", "402-555-3003"),
        (4, "James", "Young", "Manager", "Full-Time", "james.young@email.com", "402-555-3004"),
        (5, "Rachel", "King", "Client Support", "Full-Time", "rachel.king@email.com", "402-555-3005"),
        (6, "Steven", "Wright", "Security Specialist", "Contract", "steven.wright@email.com", "402-555-3006")
    ]

    sql = """
        INSERT INTO EMPLOYEE
        (employee_id, first_name, last_name, role, employment_type, email, phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(sql, employees)


def main():
    """Main program."""

    db = connect_to_database()

    if db is None:
        print("Database connection failed.")
        return

    try:
        cursor = db.cursor()

        insert_advisors(cursor)
        insert_clients(cursor)
        insert_accounts(cursor)
        insert_transactions(cursor)
        insert_appointments(cursor)
        insert_compliance_records(cursor)
        insert_employees(cursor)

        db.commit()

        print("Successfully inserted 6 records into each table.")

    except Error as e:
        db.rollback()
        print(f"Error inserting records: {e}")

    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("Database connection closed.")


if __name__ == "__main__":
    main()