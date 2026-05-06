"""
    Title: movies_update_and_delete.py
    Author: Kobe Alexander
    Date: 2026-05-02
    Description: Runs insert, update, and delete queries against the movies database.
"""

from pathlib import Path

import mysql.connector
from dotenv import dotenv_values
from mysql.connector import errorcode


def get_config():
    """Return database connection settings from .env, with class defaults as a backup."""
    env_path = Path(__file__).resolve().parent / ".env"
    secrets = dotenv_values(env_path) if env_path.exists() else {}

    #Database connection settings
    return {
        "user": secrets.get("USER", "movies_user"),
        "password": secrets.get("PASSWORD", "popcorn"),
        "host": secrets.get("HOST", "localhost"),
        "database": secrets.get("DATABASE", "movies"),
        "raise_on_warnings": secrets.get("RAISE_ON_WARNINGS", "True") == "True",
    }


def show_films(cursor, title):
    """
    Method to execute an inner join on all tables,
    iterate over the dataset, and output the results to the terminal window.
    """

    # inner join query
    cursor.execute(
        "select film_name as Name, film_director as Director, genre_name as Genre, "
        "studio_name as 'Studio Name' "
        "from film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id"
    )

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film dataset and display the results
    for film in films:
        print(
            "Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(
                film[0], film[1], film[2], film[3]
            )
        )


def main():
    """Connect to the movies database and run the required queries."""
    db = None

    try:
        db = mysql.connector.connect(**get_config())
        cursor = db.cursor()

        # Display the original list of films.
        show_films(cursor, "DISPLAYING FILMS")

        # Insert a new film. This uses an existing studio and genre from the database.
        cursor.execute(
            "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) "
            "VALUES ('Avatar', '2009', 162, 'James Cameron', "
            "(SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'), "
            "(SELECT genre_id FROM genre WHERE genre_name = 'SciFi'))"
        )
        db.commit()

        show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

        # Update Alien to being a Horror film.
        cursor.execute(
            "UPDATE film "
            "SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') "
            "WHERE film_name = 'Alien'"
        )
        db.commit()

        show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

        # Delete Gladiator.
        cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
        db.commit()

        show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password is invalid.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist.")
        else:
            print(err)

    finally:
        if db is not None and db.is_connected():
            db.close()


if __name__ == "__main__":
    main()
