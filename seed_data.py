from models import Band, Venue, Concert, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database connection and session
engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create some bands
band1 = Band(name='Arctic Monkeys', hometown='Sheffield')
band2 = Band(name='Foster the People', hometown='Los Angeles')
band3 = Band(name='Evanescence', hometown='Arkansas')

# Create some venues
venue1 = Venue(title='Red Rocks Amphitheater', city='Colorado')
venue2 = Venue(title='The Forum', city='Los Angeles')
venue3 = Venue(title='First Avenue', city='Minnesota')

# Create some concerts
concert1 = Concert(band=band1, venue=venue1, date='2024-09-25')
concert2 = Concert(band=band1, venue=venue2, date='2024-05-02')
concert3 = Concert(band=band2, venue=venue2, date='2024-07-14')
concert4 = Concert(band=band2, venue=venue1, date='2024-12-23')
concert5 = Concert(band=band3, venue=venue3, date='2024-08-25')

# Add all data to the session
session.add_all([band1, band2, band3, venue1, venue2, venue3, concert1, concert2, concert3, concert4, concert5])

# Commit the transaction to save the data to the database
session.commit()

print("Data seeded successfully!")
