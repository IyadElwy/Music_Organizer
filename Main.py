import pickle


class Song:
    def __init__(self, name: str):
        self.artist = ""
        self.name = name

    def get_song(self) -> str:
        return self.name

    def get_artist(self) -> str:
        return self.artist

    def add_artist(self, artist_name: str) -> None:
        if artist_name.isspace():
            self.artist = "Various Artists"
        else:
            self.artist = artist_name


def create_songs(binary_file_songs: str, binary_file_artist: str) -> list[Song]:
    song_names = list()
    with open(binary_file_songs, "r", encoding="utf8") as current_song, \
            open(binary_file_artist, "r", encoding="utf8") as \
                    current_artist:

        for song_line in current_song:
            song_names.append(Song(song_line[:song_line.find(
                "www.my-free-mp3.net")]))

        for index, artist_line in enumerate(current_artist):
            song_names[index].add_artist(artist_line)

    return song_names


def store_songs(songs_list: list[Song], binary_file: str) -> None:
    with open(binary_file, "wb") as songs_file:
        pickle.dump(songs_list, songs_file)


def load_songs(binary_file: str) -> list[Song]:
    with open(binary_file, "rb") as songs_file:
        songs_list = pickle.load(songs_file)
    return songs_list


def create_full_playlist(old_songs_file: str, new_songs_file: str) -> None:
    pass


if __name__ == '__main__':

    # old_songs_list = create_songs()
    # old_store_songs(songs_list)
    # old_song_names = load_songs("OldSongsObjects")
    # for index, song in enumerate(old_song_names):
    #     print(f"{index + 1}- Name: {song.name} Artist: {song.artist}")

    # new_songs_list = create_songs("new_songs_songs.txt", "new_songs_artist.txt")
    # store_songs(new_songs_list, "NewSongsObjects")
    new_song_names = load_songs("NewSongsObjects")
    for index, song in enumerate(new_song_names):
        print(f"{index + 1}- Name: {song.name} Artist: {song.artist}")
