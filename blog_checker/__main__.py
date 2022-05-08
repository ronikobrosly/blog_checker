""" Main entry point for blog checker application """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from blog_checker import BLOG_URLS, RELATIVE_PATH_TO_DB
from blog_checker.fetch_and_hash import getHash, make_request
from blog_checker.models import Base
from blog_checker.queries import insert_data, query_previous_website_entry


NEW_BLOGS_LIST = []


def main():
    """
    Top-level function of the app. Creates DB engine, creates a DB if it doesn't
    exist already (SQLite by default, but very easily changable thanks to SQLalchemy),
    loops through the list of blogs/websites and runs them through a pipeline, and then
    persists all new data to the DB.

    Args: None

    Returns: None
    """

    # Create engine for sqlalchemy
    engine = create_engine(f"sqlite:///{RELATIVE_PATH_TO_DB}", echo=False)

    # Create database if it doesn't already exist
    Base.metadata.create_all(engine)

    # Create a SQLAlchemy session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Loop through the blogs listed in BLOG_URLS dict
    for blog_name, blog_url in BLOG_URLS.items():
        pipeline(blog_name, blog_url, session)

    # Determine what will be reported to the user
    if len(NEW_BLOGS_LIST) > 0:
        print("\n------- NEW POSTS ON THE FOLLOWING WEBSITES! -------")
        for entry in NEW_BLOGS_LIST:
            print(f"* {entry}")
        print("\n\n\n")
    else:
        print("\nNo new posts on any website\n\n\n")

    engine.dispose()


def pipeline(blog_name, blog_url, session):
    """
    Runs the end-to-end pipeline of making GET request to the URL, hashing the HTML,
    checking to see if the last hash entry for that website differs from the current one,
    and writing the new hash code to the table.

    Args:
        blog_name: string, name of the website or blog
        blog_url: string, URL associated with the website or blog
        session: sqlalchemy session object

    Returns: None
    """

    # Get the HTML text for the blog
    html_text = make_request(blog_url)

    # Hash that HTML text
    hash_string = getHash(html_text)

    # Query DB for last entry for this particular website
    previous_hash_string = query_previous_website_entry(blog_name, session)

    # Create a new Websites row with today's entry
    insert_data(blog_name, blog_url, hash_string, session)

    # Commit changes to the DB
    session.commit()

    # If there is a result here, then compare it to the new hash_string
    # and if it differs, add it to the list of sites with new posts
    if previous_hash_string and (hash_string != previous_hash_string):
        NEW_BLOGS_LIST.append(blog_name)


if __name__ == "__main__":
    main()
