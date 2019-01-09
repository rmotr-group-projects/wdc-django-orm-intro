from artists.models import Artist, Song


def task_1_artists_filter_by_popularity():
    """Should return all artists that have more than 80 popularity"""
    artists_by_popularity = Artist.objects.filter(popularity__gt=80)
    return artists_by_popularity


def task_2_artists_get_by_artistic_name():
    """Should return the artist which artistic name is Jimi Hendrix"""
    artist_jimi = Artist.objects.get(artistic_name__iexact="Jimi Hendrix")
    return artist_jimi


def task_3_songs_delete():
    """Should delete all songs that contain any letter 't' in its title"""
    Song.objects.filter(title__icontains="t").delete()


def task_4_artists_create_song():
    """Should create a new song for B.B. King artist"""
    artist = Artist.objects.get(artistic_name__iexact='B.B. King')
    song = Song.objects.create()
    artist.add(song)


def task_5_artists_order_by_popularity():
    """Should return all artists ordered by popularity"""
    artists = Artist.objects.all().order_by('popularity')
    return artists


def task_6_song_edit_album(title='Superstition'):
    """Should take the song with title 'Superstition' and update its album name with any other name"""
    song = Song.objects.filter(title=title)
    song.album_name = "Supervision"


def task_7_song_counter():
    """Should return the amount of songs stored in the database"""
    num_songs = Song.objects.all().count()
    return num_songs
