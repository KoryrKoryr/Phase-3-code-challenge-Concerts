from models import Band, Venue, Concert, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database connection and session
engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

# Function to seed bands
def seed_bands(session):
    band1 = Band(name='Arctic Monkeys', hometown='Sheffield')
    band2 = Band(name='Foster the People', hometown='Los Angeles')
    band3 = Band(name='Evanescence', hometown='Arkansas')
    session.add_all([band1, band2, band3])
    session.commit()
    return band1, band2, band3

# Function to seed venues
def seed_venues(session):
    venue1 = Venue(title='Red Rocks Amphitheater', city='Colorado')
    venue2 = Venue(title='The Forum', city='Los Angeles')
    venue3 = Venue(title='First Avenue', city='Minnesota')
    session.add_all([venue1, venue2, venue3])
    session.commit()
    return venue1, venue2, venue3

# Function to seed concerts
def seed_concerts(session, bands, venues):
    concert1 = Concert(band=bands[0], venue=venues[0], date='2024-09-25')
    concert2 = Concert(band=bands[0], venue=venues[1], date='2024-05-02')
    concert3 = Concert(band=bands[1], venue=venues[1], date='2024-07-14')
    concert4 = Concert(band=bands[1], venue=venues[0], date='2024-12-23')
    concert5 = Concert(band=bands[2], venue=venues[2], date='2024-08-25')
    session.add_all([concert1, concert2, concert3, concert4, concert5])
    session.commit()

def test_band_methods(session, band1, band2, venue1, venue2):
    print("\n--- Testing Band Methods ---")
    
    # Testing `play_in_venue` method
    print(f"Testing `play_in_venue` for {band1.name}")
    band1.play_in_venue(venue1, '2025-01-01')
    new_concert = session.query(Concert).filter_by(band_id=band1.id, date='2025-01-01').first()
    print(f"New concert for {band1.name} in {venue1.title}: {new_concert.date} (Success: {new_concert is not None})")

    # Testing `all_introductions` method
    print(f"\nTesting `all_introductions` for {band1.name}")
    introductions = band1.all_introductions()
    print(f"Introductions: {introductions}")

    # Testing `most_performances` method
    print(f"\nTesting `most_performances` class method")
    most_performances_band = Band.most_performances(session)
    print(f"Band with the most performances: {most_performances_band.name}")

def test_venue_methods(session, venue1, venue2, band1):
    print("\n--- Testing Venue Methods ---")
    
    # Testing `concert_on` method
    print(f"Testing `concert_on` method for {venue1.title}")
    concert_on_date = venue1.concert_on('2024-09-25')
    print(f"Concert on 2024-09-25: {concert_on_date.band.name} (Success: {concert_on_date is not None})")

    # Testing `most_frequent_band` method
    print(f"\nTesting `most_frequent_band` method for {venue1.title}")
    most_frequent_band = venue1.most_frequent_band()
    print(f"Most frequent band at {venue1.title}: {most_frequent_band.name if most_frequent_band else 'None'}")

def test_concert_methods(session, concert):
    print("\n--- Testing Concert Methods ---")
    
    # Testing `introduction` method
    print(f"Testing `introduction` for Concert on {concert.date}")
    intro = concert.introduction()
    print(f"Introduction: {intro}")

    # Testing `hometown_show` method
    print(f"\nTesting `hometown_show` for Concert on {concert.date}")
    is_hometown = concert.hometown_show()
    print(f"Is this a hometown show? {'Yes' if is_hometown else 'No'}")


def main():
    # Seed data
    bands = seed_bands(session)
    venues = seed_venues(session)
    seed_concerts(session, bands, venues)

    # Test methods
    test_band_methods(session, bands[0], bands[1], venues[0], venues[1])
    test_venue_methods(session, venues[0], venues[1], bands[0])

    # Test Concert methods for the first concert
    concert = session.query(Concert).first()
    test_concert_methods(session, concert)

if __name__ == "__main__":
    main()
