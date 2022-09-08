from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100

date = input("What year would you like to travel to in? (YYYY-MM-DD) ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(billboard_url)
billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")
# print(soup.prettify())
song_titles = soup.select(".o-chart-results-list__item h3")
song_names = [title.get_text(strip=True) for title in song_titles]
#print(song_names)

#Spotify Authentication

client_id = "6b7646aa7040424e8ad3a8e50fc86a62"
client_secret = "f142114cd64347db989d6ea4313b446c"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

#Searching Spotify for songs by title

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
