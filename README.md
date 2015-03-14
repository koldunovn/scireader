# scireader
Monitor and display new content from scientific journals.

The app gets information about new publications from RSS feeds of scientific journals and puts them in to a database. Then publications with predefined key-words in the title or the abstract are displayed. In addition you can search for arbitrary key-words.

Example: http://178.62.254.199/

This is a very simple Flask/MongoDB application, that I initially wrote for educational purposes, but that turned to be useful other people.

## Dependencies:

- MongoDB
- apache2
- libapache2-mod-wsgi

#### Python
- Flask
- PyMongo
- feedparser

## Configuration

To change list of journals, just edit 
`/FlaskApp/static/journal_list.json`

To change the list of key-words, you have to edit `rssreader/getdata.py` (`find_terms` calls) and modify `/FlaskApp/__init__.py` 

In order to update database regularly, you have to setup cron job, that runs `rssreader/getdata.py` 

## Screenshots
###Predefined key-word:
![Alt text](/../screenshots/screenshots/key_word.png?raw=true "Predefined key-word" )

###List of journals:
![Alt text](/../screenshots/screenshots/journals.png?raw=true "List of journals")

###Search:
![Alt text](/../screenshots/screenshots/search.png?raw=true "Search")

###Search results:
![Alt text](/../screenshots/screenshots/search_results.png?raw=true "Search results")
