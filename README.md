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
