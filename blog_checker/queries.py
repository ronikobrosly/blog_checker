""" This module contains all sqlalchemy queries """

from datetime import datetime

from sqlalchemy import desc

from blog_checker import TIMEZONE
from blog_checker.models import Websites


def insert_data(blog_name, blog_url, hash_string, session):
    """
    Inserts a new row into DB

    Args:
        blog_name: string, name of the website or blog
        blog_url: string, URL associated with the website or blog
        hash_string: string, a hash string
        session: sqlalchemy session object

    Returns: None
    """

    new_website_data = Websites(
        website_name=blog_name,
        website_url=blog_url,
        date_retrieved=datetime.now(TIMEZONE),
        hash=hash_string,
    )
    session.add(new_website_data)


def query_previous_website_entry(blog_name, session):
    """
    Takes a particular website, queries the previous entry from at the day before and back,
    and pulls the hash string that from last entry.

    Args:
        blog_name: string, name of the website or blog
        session: sqlalchemy session object

    Returns:
        The previous hash string associated with the website
    """

    # Run query on table
    results = (
        (session.query(Websites).filter(Websites.website_name == blog_name))
        .order_by(desc(Websites.date_retrieved))
        .first()
    )

    # If the query finds a result, return the hash in that result
    if results:
        return results.hash

    # Otherwise return a None object
    return results
