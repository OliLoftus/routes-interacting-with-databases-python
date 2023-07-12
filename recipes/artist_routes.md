# {{ NAME }} Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```

GET /artists


POST /artists
    name: string
    genre: string
    

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# Albums route
Get /artists

# add album route
POST /artists


# EXAMPLE TESTS

# GET /artists
#  Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone
"""

# Post /artists
# Parameters:
# name: Wild nothing
# genre: indie
#  Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""

# POST /artists
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide an artist and genre
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

"""
GET /artists
  Expected response (200 OK):
  All artists
"""
def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/album_library.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"



"""
POST /artists with data
  Expected response (200 OK):
"""

def test_post_artists(web_client, db_connection):
    db_connection.seed('seeds/album_library.sql')
    post_response = web_client.post('/artists', data = {'name': 'Wild nothing', 'genre': 'indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"


"""
POST /artists without data
Expected response (400)
"Please provide an artist and genre"
"""
def test_post_artists_with_no_data(web_client, db_connection):
    db_connection.seed('seeds/album_library.sql')
    post_response = web_client.post('/artists')
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == 'You need to submit a title, release_year and artist_id.'
```


