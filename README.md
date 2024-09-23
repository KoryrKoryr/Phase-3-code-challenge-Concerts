# Phase-3-code-challenge-Concerts

This code challenge is a simple music concert management system using SQLAlchemy ORM in Python. It consists of three main models: `Band`, `Venue`, and `Concert`.

## Models

### Band

- `id`: Primary key for the band.
- `name`: Name of the band.
- `hometown`: Hometown of the band.
- `concerts`: Relationship with the `Concert` model, representing all concerts performed by the band.

### Venue

- `id`: Primary key for the venue.
- `title`: Title of the venue.
- `city`: City where the venue is located.
- `concerts`: Relationship with the `Concert` model, representing all concerts held at the venue.

### Concert

- `id`: Primary key for the concert.
- `date`: Date of the concert.
- `band_id`: Foreign key referencing the `Band` model.
- `venue_id`: Foreign key referencing the `Venue` model.
- `band`: Relationship with the `Band` model, representing the band performing at the concert.
- `venue`: Relationship with the `Venue` model, representing the venue where the concert is held.

## Methods

### Band

- `concerts()`: Returns all concerts performed by the band.
- `venues()`: Returns a list of unique venues where the band has performed.
- `play_in_venue(venue, date)`: Creates a new concert for the band at the specified venue and date.
- `all_introductions()`: Returns a list of introductions for all concerts performed by the band.
- `most_performances(session)`: Class method that returns the band with the most concerts in the given session.

### Venue

- `concerts()`: Returns all concerts held at the venue.
- `bands()`: Returns a list of unique bands that have performed at the venue.
- `concert_on(date)`: Returns the concert held at the venue on the specified date, or `None` if no such concert exists.
- `most_frequent_band()`: Returns the band that has performed at the venue most frequently.

### Concert

- `band()`: Returns the band performing at the concert.
- `venue()`: Returns the venue where the concert is held.
- `hometown_show()`: Returns `True` if the concert is a hometown show, `False` otherwise.
- `introduction()`: Returns an introduction for the concert.# Phase-3-code-challenge-Concerts

## Setup And Installation

### Clone the repository

- `git clone https://github.com/KoryrKoryr/Phase-3-code-challenge-Concerts.git`
- `cd Phase-3-code-challenge-Concerts`

### Setup virtual environment and install dependancies

-This project uses Pipenv for managing the virtual environment and dependencies. Install Pipenv if you don’t have it:

- `pip install pipenv`

Install the dependencies:

- `pipenv install`

### Activate the virtual environment

- `pipenv shell`

## Database Setup

SQLite is used for the database. Make sure to initialize the database with the required tables by running Alembic migrations.

- Run the migrations to create the database schema.
  - `alembic upgrade head`
- This will create the necessary tables (bands, concerts and venues), if they are not already created.

## Sample Seed Data and Testing of Methods

Sample data and testing methods have been written in the `seed_data.py` file.

**Seeding Data:**

- `seed_bands(session)`: Creates and adds three Band objects to the database.
- `seed_venues(session)`: Creates and adds three Venue objects to the database.
- `seed_concerts(session, bands, venues)`: Creates and adds five Concert objects that relate to the seeded bands and venues.

**Testing Methods:**

- `test_band_methods(session, band1, band2, venue1, venue2)`: Tests the following `Band` methods:
  - `play_in_venue`: Adds a new concert for a band and checks if it was successfully added.
  - `all_introductions`: Retrieves all concert introductions for a band.
  - `most_performances`: Finds the band with the most performances.
- test_venue_methods(session, venue1, venue2, band1): Tests the following `Venue` methods:
  - `concert_on`: Finds the concert on a specific date.
  - `most_frequent_band`: Finds the band that performed most often at the venue.
- test_concert_methods(session, concert): Tests the following `Concert` methods:
  - `introduction`: Generates an introduction string for the concert.
  - `hometown_show`: Checks if the concert is in the band's hometown.

### Running the script:

To add seed data and run tests for the methods, run the following command:

- `python seed_data.py`

### Expected output:

The output will show the seeded data being created and the results of your method tests, such as whether the concert was added successfully, whether the introductions are correct, and which band has the most performances.

Here is how the output should look like:

```
Starting to seed data...
Bands added to the session.
Bands committed to the database.
Venues added to the session.
Venues committed to the database.
Concerts added to the session.
Concerts committed to the database.
Data seeded successfully!

--- Testing Band Methods ---
Testing `play_in_venue` for Arctic Monkeys
New concert for Arctic Monkeys in Red Rocks Amphitheater: 2025-01-01 (Success: True)

Testing `all_introductions` for Arctic Monkeys
Introductions: ["Hello Colorado!!!!! We are Arctic Monkeys and we're from Sheffield", "Hello Los Angeles!!!!! We are Arctic Monkeys and we're from Sheffield", "Hello Colorado!!!!! We are Arctic Monkeys and we're from Sheffield"]

Testing `most_performances` class method
Band with the most performances: Arctic Monkeys

--- Testing Venue Methods ---
Testing `concert_on` method for Red Rocks Amphitheater
Concert on 2024-09-25: Arctic Monkeys (Success: True)

Testing `most_frequent_band` method for Red Rocks Amphitheater
Most frequent band at Red Rocks Amphitheater: Arctic Monkeys

--- Testing Concert Methods ---
Testing `introduction` for Concert on 2024-09-25
Introduction: Hello Colorado!!!!! We are Arctic Monkeys and we're from Sheffield

Testing `hometown_show` for Concert on 2024-09-25
Is this a hometown show? No
```
