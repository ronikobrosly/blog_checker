"""
This module contains the Websites model for the database
"""

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Websites(Base):
    """
    Model associated with the `websites` table in the database
    """

    __tablename__ = "websites"
    website_id = Column(Integer, primary_key=True)
    website_name = Column(String)
    website_url = Column(String)
    date_retrieved = Column(DateTime)
    hash = Column(String)
