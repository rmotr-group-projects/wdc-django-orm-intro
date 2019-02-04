from artists.models import Artist, Song


def task_1_artists_filter_by_popularity():
    """Should return all artists that have more than 80 popularity"""
    artists = Artist.objects.filter(popularity__gt=80)
    return artists


def task_2_artists_get_by_artistic_name():
    """Should return the artist which artistic name is Jimi Hendrix"""
    artist = Artist.objects.get(artistic_name='Jimi Hendrix')
    return artist


def task_3_songs_delete():
    """Should delete all songs that contain any letter 't' in its title"""
    songs = Song.objects.filter(title__icontains='t')
    songs.delete()


def task_4_artists_create_song():
    """Should create a new song for B.B. King artist"""
    new_song = Song.objects.create(artist_id=3, title='Sweet Little Angel', album_name='Some B.B. King album')


def task_5_artists_order_by_popularity():
    """Should return all artists ordered by popularity"""
    artists_by_pop = Artist.objects.order_by('popularity')
    return artists_by_pop


def task_6_song_edit_album():
    """Should take the song with title 'Superstition' and update its album name with any other name"""
    update_song = Song.objects.get(title__icontains='Superstition')
    update_song.album_name = 'Some other album'
    update_song.save()
    return update_song


def task_7_song_counter():
    """Should return the amount of songs stored in the database"""
    all_songs = Song.objects.all().count()
    return all_songs
