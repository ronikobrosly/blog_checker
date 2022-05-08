"""blog_checker init statements"""

import pytz


# What is the relative path to the database
RELATIVE_PATH_TO_DB = "blogs.db"

# To see a list of all common timezones, use command `print(pytz.common_timezones)`
TIMEZONE = pytz.timezone("US/Eastern")

# Dictionary of blogs/websites and their URLs
BLOG_URLS = {
    "Sebastian Raschka Blog": "https://sebastianraschka.com/blog/index.html",
    "Erik Bernhardsson Blog": "https://www.erikbern.com/",
    "Locally Optimistic": "https://locallyoptimistic.com/",
}
