from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta

Base: DeclarativeMeta = declarative_base()

# Band Model
class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
    
    concerts = relationship('Concert', back_populates='band')

    # Returns all venues where the band has performed
    def venues(self):
        return list({concert.venue for concert in self.concerts})

    # Create a concert at a given venue on a specific date
    def play_in_venue(self, venue, date):
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)
        session.commit()

    # Get all introductions for this band's concerts
    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    # Class method to find the band with the most performances
    @classmethod
    def most_performances(cls, session):
        bands = session.query(cls).all()
        return max(bands, key=lambda band: len(band.concerts))

# Venue Model
class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)
    
    concerts = relationship('Concert', back_populates='venue')

    # Get all bands that performed at this venue
    def bands(self):
        return list({concert.band for concert in self.concerts})

    # Find a concert at this venue on a specific date
    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)

    # Find the band with the most concerts at this venue
    def most_frequent_band(self):
        from collections import Counter
        band_counts = Counter(concert.band for concert in self.concerts)
        return band_counts.most_common(1)[0][0] if band_counts else None

# Concert Model
class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    # Return the band for this concert
    def band(self):
        return self.band
    
    # Return the venue for this concert
    def venue(self):
        return self.venue
    
    # Check if the concert is in the band's hometown
    def hometown_show(self):
        return self.venue.city == self.band.hometown
    
    # Return an introduction for the concert
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

# Setup SQLite in-memory database (or replace with your own DB URI)
engine = create_engine('sqlite:///concerts.db', echo=True)
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Seed some data for testing
def seed_data():
    band1 = Band(name='The Cool Band', hometown='New York')
    band2 = Band(name='Rock Stars', hometown='Los Angeles')

    venue1 = Venue(title='Madison Square Garden', city='New York')
    venue2 = Venue(title='The Forum', city='Los Angeles')

    concert1 = Concert(band=band1, venue=venue1, date='2024-09-15')
    concert2 = Concert(band=band1, venue=venue2, date='2024-10-12')
    concert3 = Concert(band=band2, venue=venue2, date='2024-11-01')

    session.add_all([band1, band2, venue1, venue2, concert1, concert2, concert3])
    session.commit()

if __name__ == "__main__":
    # Seed data into the database
    seed_data()

    # Example: Find all venues for a band
    cool_band = session.query(Band).filter_by(name='The Cool Band').first()
    print(f"Venues for {cool_band.name}: {cool_band.venues()}")

    # Example: Get the introduction for the first concert
    concert = session.query(Concert).first()
    print(f"Concert introduction: {concert.introduction()}")

    # Example: Find the most frequent band at a venue
    forum = session.query(Venue).filter_by(title='The Forum').first()
    print(f"Most frequent band at {forum.title}: {forum.most_frequent_band().name}")
    
    # Example: Find the band with the most performances
    band_with_most_performances = Band.most_performances(session)
    print(f"Band with the most performances: {band_with_most_performances.name}")
