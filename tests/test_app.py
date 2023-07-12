# Tests for your routes go here

"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    # We'll simulate sending a GET request to /wave?name=Dana
    # This returns a response object we can test against.
    response = web_client.get('/wave?name=Dana')

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'I am waving at Dana'

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    # We'll simulate sending a POST request to /submit with a name and message
    # This returns a response object we can test against.
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'

    """
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

#tests

#POST route
#POST  /sort-names
#POST 'names=<list>' /sort-names

def test_sort_list_alphabetically(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran' })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Joe, Julia, Kieran, Zoe'

"""
When i call GET /albums i get a list of albums
"""
def test_get_albums(web_client, db_connection):
    db_connection.seed('seeds/album_library.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album one, released: 2022, artist: 1\n" \
        "Album two, released: 2021, artist: 2\n" \
        "Album three, released: 2018, artist: 1\n" \
        "Album four, released: 2000, artist: 3\n" \
    

"""
When I call POST /albums with album info that album
is now in the GET /albums list
"""

def test_post_albums(web_client, db_connection):
    db_connection.seed('seeds/album_library.sql')
    post_response = web_client.post('/albums', data = {'title': 'Album ten', 'release_year': '2010', 'artist_id': '1'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == 'Album added successfully.'

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album one, released: 2022, artist: 1\n" \
        "Album two, released: 2021, artist: 2\n" \
        "Album three, released: 2018, artist: 1\n" \
        "Album four, released: 2000, artist: 3\n" \
        "Album ten, released: 2010, artist: 1\n"
    
"""
When a post call is made with no data we get a 400
and an error message
"""

def test_post_albums_with_no_data(web_client, db_connection):
    db_connection.seed('seeds/album_library.sql')
    post_response = web_client.post('/albums')
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == 'You need to submit a title, release_year and artist_id.'

"""
When a Get call is made we get artists back
"""
def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/album_library.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "1. Pixies 2. ABBA 3. Taylor Swift 4. Nina Simone "

"""
When a POST /artists is made with data, the 
artist is added to database
"""
def test_post_artists(web_client, db_connection):
    db_connection.seed('seeds/album_library.sql')
    post_response = web_client.post('/artists', data = {'name': 'Wild nothing', 'genre': 'indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "1. Pixies 2. ABBA 3. Taylor Swift 4. Nina Simone 5. Wild nothing "

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"







# === End Example Code ===
