from models import Band, Venue, Concert, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Set up the database connection and session
engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_bands(session):
    """Create and add bands to the session."""
    bands = [
        Band(name='Arctic Monkeys', hometown='Sheffield'),
        Band(name='Foster the People', hometown='Los Angeles'),
        Band(name='Evanescence', hometown='Arkansas')
    ]
    
    session.add_all(bands)
    print("Bands added to the session.")
    return bands

def seed_venues(session):
    """Create and add venues to the session."""
    venues = [
        Venue(title='Red Rocks Amphitheater', city='Colorado'),
        Venue(title='The Forum', city='Los Angeles'),
        Venue(title='First Avenue', city='Minnesota')
    ]
    
    session.add_all(venues)
    print("Venues added to the session.")
    return venues

def seed_concerts(session, bands, venues):
    """Create and add concerts to the session."""
    concerts = [
        Concert(band=bands[0], venue=venues[0], date='2024-09-25'),
        Concert(band=bands[0], venue=venues[1], date='2024-05-02'),
        Concert(band=bands[1], venue=venues[1], date='2024-07-14'),
        Concert(band=bands[1], venue=venues[0], date='2024-12-23'),
        Concert(band=bands[2], venue=venues[2], date='2024-08-25')
    ]
    
    session.add_all(concerts)
    print("Concerts added to the session.")

def main():
    """Main seeding function."""
    try:
        # Seed the data
        print("Starting to seed data...")
        bands = seed_bands(session)
        venues = seed_venues(session)
        session.commit()  # Commit to get the IDs assigned to bands and venues
        print("Bands and venues committed to the database.")
        
        seed_concerts(session, bands, venues)
        session.commit()  # Commit the concerts
        print("Concerts committed to the database.")
        
        print("Data seeded successfully!")
    
    except SQLAlchemyError as e:
        session.rollback()  # Roll back the session in case of an error
        print(f"An error occurred: {e}")
    
    finally:
        session.close()  # Ensure the session is closed

if __name__ == "__main__":
    main()
