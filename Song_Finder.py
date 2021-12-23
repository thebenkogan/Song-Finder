import requests
from bs4 import BeautifulSoup
import speech_recognition as sr

re = sr.Recognizer()
with sr.Microphone() as source:
    print("Say song lyrics: ")
    audio = re.listen(source)

try:
    lyrics = re.recognize_google(audio)
except Exception:
    print("Google could not understand what you said.")

print("The lyrics you said: " + lyrics + "\n")

url = "https://www.lyrics.com/subserp.php"
PARAMS = {"st": lyrics}
r = requests.get(url, PARAMS)
print("Website visited: " + r.url + "\n")

soup = BeautifulSoup(r.text, "html.parser")
song_names = soup.find_all("p", class_="lyric-meta-title")
song_artists = soup.find_all(
    "p", class_=["lyric-meta-album-artist", "lyric-meta-artists"]
)

names = []
artists = []

for name in song_names:
    names.append(name.text)

for artist in song_artists:
    artists.append(artist.text)

print("The top 3 songs associated with those lyrics as suggested by lyrics.com are: ")
print("1.) " + names[0] + " by " + artists[0])
print("2.) " + names[1] + " by " + artists[1])
print("3.) " + names[2] + " by " + artists[2])
