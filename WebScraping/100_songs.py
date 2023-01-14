from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIEND_ID = "00c2dbc566e44eb781d3bb6b1a2dadaf"
SPOTIFY_CLIEND_SECRET = "68e50e41ae14405fb167cd4631fb15c3"

# Getting the website of the selected date's HTML
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")
song_names = [
    element.getText().removeprefix('\n\n\t\n\t\n\t\t\n\t\t\t\t\t').removesuffix('\t\t\n\t\n')
    for element in soup.select(".o-chart-results-list__item #title-of-a-story")
]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIEND_ID,
        client_secret=SPOTIFY_CLIEND_SECRET,
        show_dialog=True,
        cache_path=".cache"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for name in song_names:
    result = sp.search(q=f"track:{name} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{name} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

