import requests
import sqlite3

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

response = requests.get(url, headers={'Accept':'application/json'}, params={
    'format':'geojson',
    'starttime':input('enter the start time (YYYY-MM-DD) '),
    'endtime':input('enter the end time (YYYY-MM-DD) '),
    'latitude':input('enter the latitude '),
    'longitude':input('enter the longitude '),
    'maxradiuskm':input('enter max radius in km '),
    'minmagnitude':input('enter min magnitude ')
})

data = response.json()

earthquake_list = data['features']
count = 0
for earthquake in earthquake_list:
    count +=1
    num = count
    place = earthquake["properties"]["place"]
    mag = earthquake["properties"]["mag"]
    result = (num, place, mag)
    # print(f'{count}. Place: {earthquake["properties"]["place"]}. Magnitude: {earthquake["properties"]["mag"]}.')


    conn = sqlite3.connect('earthquakes_db.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE quakes (id INTEGER, place TEXT, magnitude REAL);")
    insert_values = "INSERT INTO quakes VALUES(?, ?, ?);"

    cursor.execute(insert_values, result)

    conn.commit()
    conn.close()


