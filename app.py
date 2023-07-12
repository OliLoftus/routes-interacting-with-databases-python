import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

# # Request:
# POST /submit
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
# # With body parameters:
# name=Leo
# message=Hello world
    return f'Thanks {name}, you sent this message: "{message}"'
# # Expected response (2OO OK):
# Thanks Leo, you sent this message: "Hello world"

# # Request:
# GET /wave?name=Leo
@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
# # Expected response (200 OK):
# I am waving at Leo
    return f"I am waving at {name}"
# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    count = 0
    for c in text:
        if c in 'aeiou':
            count += 1
    return f'There are {count} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['names']
    print(names)
    split_names = names.split(",")
    print(split_names)
    sort_names = sorted(split_names)
    print(sort_names)
    return ', '.join(sort_names)

# music_library routes

@app.route('/albums', methods=['POST'])
def post_albums():
    if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
        return 'You need to submit a title, release_year and artist_id.', 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)
    return 'Album added successfully.'

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    result_string = ""
    for album in albums:
        result_string += str(f"{album}\n")
    return result_string

# GET /artists

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    result_string = ""
    for artist in artists:
        print(artist)
        result_string += f"{artist.id}. {artist.name} "
    return result_string

# POST /artists

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form['name'],
        request.form['genre'],)
    repository.create(artist)
    return ''


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

