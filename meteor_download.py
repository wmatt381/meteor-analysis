#!/usr/bin/env python3

import json
import urllib.request, urllib.parse, urllib.error
import http
import ssl
import sys
import sqlite3
from sql_func import createTable

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get json file for analysis
url = input('Enter json url:')
if url == '':
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
print('Attempting to open json from:', url)

# Attempt to load json
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
js = json.loads(data)
# Get json file name from url
file_name = url.split('/')[-1]
print(file_name, 'successfully loaded')

# Initialize sql and connect to database
conn = sqlite3.connect('nasaMeteor.sqlite')
cur = conn.cursor()

# Define table name and columns for SQL table (table_name, column1, column2, etc.)
columns = ('meteor_landings', 'id INTEGER UNIQUE', 'name TEXT', 'nametype TEXT',
     'recclass TEXT', 'mass INTEGER', 'fall TEXT', 'year TEXT', 'reclat REAL', 'reclong REAL')

# Create table
cur.execute(createTable(*columns))

# Resume data download if interrupted
start = None
cur.execute('SELECT max(id) FROM meteor_landings' )
try:
    row = cur.fetchone()
    if row is None :
        start = 0
    else:
        start = row[0]
except:
    start = 0

if start is None : start = 0

count = 0 # Track number of entries performed

# Function to check for missing key data
def check_data(entry, key):
    if entry.get(key) == None : value = 'Null'
    else : value = entry[key]
    return value

# Iterate json file and extract values to database
for entry in js:
    name = check_data(entry, 'name')
    nametype = check_data(entry, 'nametype')
    recclass = check_data(entry, 'recclass')
    mass = check_data(entry, 'mass')
    fall = check_data(entry, 'fall')
    year = check_data(entry, 'year')
    reclat = check_data(entry,'reclat')
    reclong = check_data(entry, 'reclong')

    count = count + 1
    #print(name, nametype, recclass, mass, fall, year, reclat, reclong)
    # Insert values into table
    cur.execute('''INSERT OR IGNORE INTO meteor_landings (id, name, nametype, recclass, mass, fall, year,
        reclat, reclong) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (start, name, nametype, recclass, mass, fall, year, reclat, reclong))
    if count % 50 == 0 : conn.commit() # Commit table insertions every 50 entries
    start = start + 1

# Final commit and close
conn.commit()
cur.close()

print('Database successfully created and uploaded with data from:', file_name)
