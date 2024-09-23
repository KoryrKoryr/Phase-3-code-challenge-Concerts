from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from database import session

Base = declarative_base()

# Band Model
class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
    
    concerts_relationship = relationship('Concert', back_populates='band')

    def get_concerts(self):
        """Returns all concerts for the band."""
        return self.concerts_relationship

    def get_venues(self):
        """Returns all venues the band has played at."""
        return list({concert.venue for concert in self.concerts_relationship})

    def play_in_venue(self, venue, date, session):
        """Creates a new concert for the band at the given venue and date."""
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)
        session.commit()  # Consider moving session handling outside the model

    def all_introductions(self):
        """Returns introductions for all the band's concerts."""
        return [concert.introduction() for concert in self.concerts_relationship]

    @classmethod
    def most_performances(cls, session):
        """Returns the band with the most performances."""
        bands = session.query(cls).all()
        return max(bands, key=lambda band: len(band.concerts_relationship))

# Venue Model
class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)
    
    concerts_relationship = relationship('Concert', back_populates='venue')

    def get_concerts(self):
        """Returns all concerts at the venue."""
        return self.concerts_relationship

    def get_bands(self):
        """Returns all bands that performed at the venue."""
        return list({concert.band for concert in self.concerts_relationship})

    def concert_on(self, date):
        """Finds and returns the first concert on the given date."""
        return next((concert for concert in self.concerts_relationship if concert.date == date), None)

    def most_frequent_band(self):
        """Returns the band with the most concerts at this venue."""
        from collections import Counter
        band_counts = Counter(concert.band for concert in self.concerts_relationship)
        return band_counts.most_common(1)[0][0] if band_counts else None

# Concert Model
class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    band = relationship('Band', back_populates='concerts_relationship')
    venue = relationship('Venue', back_populates='concerts_relationship')

    def get_band(self):
        """Returns the band for the concert."""
        return self.band

    def get_venue(self):
        """Returns the venue for the concert."""
        return self.venue

    def hometown_show(self):
        """Returns true if the concert is in the band's hometown."""
        return self.venue.city == self.band.hometown

    def introduction(self):
        """Returns a string with the band's introduction for the concert."""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
