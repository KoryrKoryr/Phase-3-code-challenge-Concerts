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
    
    concerts = relationship('Concert', back_populates='band')

    def concerts(self):
        return self.concerts

    def venues(self):
        return list({concert.venue for concert in self.concerts})

    def play_in_venue(self, venue, date):
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)
        session.commit()

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

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

    def concerts(self):
        return self.concerts

    def bands(self):
        return list({concert.band for concert in self.concerts})

    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self):
        from collections import Counter
        band_counts = Counter(concert.band for concert in self.concerts)
        return band_counts.most_common(1)[0][0] if band_counts else None

# Concert Model
class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def band(self):
        return self.band

    def venue(self):
        return self.venue

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
