import webbrowser

music = {
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "ncs": "https://www.youtube.com/watch?v=2vjPBrBU-TM"
}


def play(song):
    song = song.lower()
    for name, url in music.items():
        if song in name:
            webbrowser.open(url)
            return True
    return False
