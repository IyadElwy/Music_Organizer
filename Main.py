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
    list_with_found_song_indexes = list()
    list_with_missing_song_indexes = list()
    num_of_found_songs = 0

    old_song_names = load_songs(old_songs_file)
    new_song_names = load_songs(new_songs_file)

    for index, old_song in enumerate(old_song_names):
        for new_song in new_song_names:
            if old_song.get_song() == new_song.get_song():
                num_of_found_songs += 1
                list_with_found_song_indexes.append(index)

    for i in range(len(old_song_names)):
        if i not in list_with_found_song_indexes:
            list_with_missing_song_indexes.append(i)

    for i in list_with_missing_song_indexes:
        print(old_song_names[i].get_song())

    print(list_with_missing_song_indexes)


if __name__ == '__main__':
    # print("Welcome to Music Organizer!\n")
    # old_songs_file_path_songs = input("Please enter the path of the "
    #                                   "file\nwith the song names you wish to "
    #                                   "compare:\n")
    # old_songs_file_path_artists = input("Please enter the path of the "
    #                                     "file\nwith the corresponding artist "
    #                                     "names:\n")
    # new_songs_file_path_songs = input("Please enter the path of the "
    #                                   "file\nwith the song names you wish to "
    #                                   "compare:\n")
    # new_songs_file_path_artists = input("Please enter the path of the "
    #                                     "file\nwith the corresponding artist "
    #                                     "names:\n")
    # print("\nChecking...\n\n\n")
    #
    # old_songs = create_songs(old_songs_file_path_songs,
    #                          old_songs_file_path_artists)
    # store_songs(old_songs, "OldSongsObjects")
    #
    # new_songs = create_songs(new_songs_file_path_songs,
    #                          new_songs_file_path_artists)
    # store_songs(old_songs, "NewSongsObjects")

    create_full_playlist("OldSongsObjects", "NewSongsObjects")
