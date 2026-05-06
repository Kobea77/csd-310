import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

env_path = os.path.join(os.path.dirname(__file__), ".env")

print("Looking for .env at:", env_path)
print("File exists?", os.path.exists(env_path))

with open(env_path, "rb") as file:
    print(file.read())

secrets = dotenv_values(env_path)

print("Secrets loaded:", secrets)

config = {
    "user": secrets.get("USER"),
    "password": secrets.get("PASSWORD"),
    "host": secrets.get("HOST"),
    "database": secrets.get("DATABASE"),
    "raise_on_warnings": secrets.get("RAISE_ON_WARNINGS") == "True"
}

if not all([config["user"], config["password"], config["host"], config["database"]]):
    print("Error: Missing one or more values from the .env file.")
    exit()

db = None

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()

    print("\n-- DISPLAYING Studio RECORDS --")

    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}")
        print()

    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()

    print("-- DISPLAYING Genre RECORDS --")

    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}")
        print()

    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()

    print("-- DISPLAYING Short Film RECORDS --")

    for film in short_films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}")
        print()

    cursor.execute("""
        SELECT film_name, film_director
        FROM film
        ORDER BY film_director
    """)

    directors = cursor.fetchall()

    print("-- DISPLAYING Director RECORDS in Order --")

    for director in directors:
        print(f"Film Name: {director[0]}")
        print(f"Director: {director[1]}")
        print()

    cursor.close()

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