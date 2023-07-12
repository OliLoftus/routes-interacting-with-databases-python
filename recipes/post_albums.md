# {{ NAME }} Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```

POST /albums


POST /albums
    title: string
    release_year: int
    artist_id: int

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# Albums route
Get /albums

# add album route
POST /albums


# EXAMPLE TESTS

# GET /albums
#  Expected response (200 OK):
"""
All albums
"""

# Post /albums
# Parameters:
# title: Album ten
# release_year: 2022
# artist_id: 1
#  Expected response (200 OK):
"""
Album ten, released: 2022, artist: 1
"""

# Post /albums
# Parameters:
# title: Album five
# release_year: 1990
# artist_id: 3
#  Expected response (200 OK):
"""
Album one, released: 2022, artist: 1
"""

# POST /albums
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a title, release year and an artist id
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

"""
GET /albums
  Expected response (200 OK):
  All albums
"""
def test_get_albums(web_client):
    #seed
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == """
    Album one, released: 2022, artist: 1
    Album two, released: 2021, artist: 2
    Album three, released: 2018, artist: 1
    Album four, released: 2000, artist: 3
    """



"""
POST /albums
  Expected response (200 OK):
  "Album ten, released: 2022, artist: 1"
"""

def test_post_album(web_client):
    #seed
    response = web_client.post('/albums', data = {'title': 'Album ten', 'release_year': '2022', 'artist_id': '1'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Album added successfully.'

    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == """
    Album one, released: 2022, artist: 1
    Album two, released: 2021, artist: 2
    Album three, released: 2018, artist: 1
    Album four, released: 2000, artist: 3
    Album ten, released: 2022, artist: 1
    """
    
```

