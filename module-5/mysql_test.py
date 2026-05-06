import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), ".env")

loaded = load_dotenv(env_path)
print("Did .env load?", loaded)

print("USER =", os.getenv("USER"))
print("PASSWORD =", os.getenv("PASSWORD"))
print("HOST =", os.getenv("HOST"))
print("DATABASE =", os.getenv("DATABASE"))

config = {
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "host": os.getenv("HOST"),
    "database": os.getenv("DATABASE"),
    "raise_on_warnings": True
}

if not all([config["user"], config["password"], config["host"], config["database"]]):
    print("Error: Missing one or more values from the .env file.")
    exit()

db = None

try:
    db = mysql.connector.connect(**config)

    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]
    ))

    input("\nPress Enter to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    if db is not None and db.is_connected():
        db.close()
        print("Connection closed.")