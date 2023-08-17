from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Last.fm API base URL
LASTFM_BASE_URL = "http://ws.audioscrobbler.com/2.0/"

# Last.fm API key (replace with your actual API key)
LASTFM_API_KEY = "4e8e5b4b9ac9c01a00a2cd05dcc03226"

@app.route("/", methods=["GET", "POST"])
def index():
    top_tracks = []
    if request.method == "POST":
        artist_name = request.form.get("artist_name")
        if artist_name:
            top_tracks = get_top_tracks(artist_name)
    return render_template("index.html", top_tracks=top_tracks)

def get_top_tracks(artist_name):
    params = {
        "method": "artist.gettoptracks",
        "artist": artist_name,
        "api_key": LASTFM_API_KEY,
        "format": "json"
    }
    response = requests.get(LASTFM_BASE_URL, params=params)
    data = response.json()
    if "toptracks" in data and "track" in data["toptracks"]:
        return data["toptracks"]["track"]
    return []

if __name__ == "__main__":
    app.run(debug=True)
