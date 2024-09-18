from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Band Model
class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
    
    # Relationship to Concerts
    concerts = relationship('Concert', back_populates='band')
    
    # Helper method to get all venues
    def venues(self):
        return list({concert.venue for concert in self.concerts})

# Venue Model
class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)
    
    # Relationship to Concerts
    concerts = relationship('Concert', back_populates='venue')
    
    # Helper method to get all bands that performed here
    def bands(self):
        return list({concert.band for concert in self.concerts})

# Concert Model
class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)  # or DateTime for date format
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    
    # Relationships
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    # Methods
    def band(self):
        return self.band
    
    def venue(self):
        return self.venue
    
    def hometown_show(self):
        return self.venue.city == self.band.hometown
    
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

