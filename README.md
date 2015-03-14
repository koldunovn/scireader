# scireader
Monitor and display new content from scientific journals.

The app gets information about new publications from RSS feeds of scientific journals and puts them in to a data base. Then publications with predefined key-words in the title or the abstract are displayed. In addition you can search for arbitrary key-words.

This is a very simple Flask/MongoDB application, that I initially wrote for educational purposes, but that turned to be useful other people.

## Dependencies:

- MongoDB
- apache2
- libapache2-mod-wsgi

#### Python
- Flask
- PyMongo
- feedparser
