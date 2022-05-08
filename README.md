# blog-checker

## Overview

Not all data, tech leadership, and engineering blogs have an option to subscribe and receive email updates on new blog posts. And some of the best personal blogs out there only drop a few times a year. You're then forced to periodically and manually check these websites for updates. If you have dozens of these personal sites and blogs that you like, that sucks.  

Blog Checker is a tool to automate the process of checking personal websites and blogs for updates. More generally,
it can be used to check if changes have occurred on any type of website.

## Installation

Blog Checker requires python 3.9+ and an internet connection.

Create your a virtual environment using your tool of choice, navigate to the root folder of
`blog_checker` and run `pip install -r requirements.txt`.

That's all! 😎

## Instructions

Open the `__init__.py` file within the project's `blog_checker` folder. This file serves as a
config file for the project. Update the following global variables as you see fit:

- `RELATIVE_PATH_TO_DB`: Describe the relative path (relative to the root project folder) where the database is located or will be created
- `TIMEZONE`: Specify your timezone (default is US Eastern)
- `BLOG_URLS`: Fill in this dictionary with the names of your blog sites (keys) and their URLs (values). The URLs should be the page on the site that lists various blog entries (e.g. `https://sebastianraschka.com/blog/index.html`)

Once done with this, simply navigate to the root project folder and run `python -m blog_checker`
