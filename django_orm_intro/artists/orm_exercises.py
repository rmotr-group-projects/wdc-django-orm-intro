from artists.models import Artist, Song


def task_1_artists_filter_by_popularity():
    return Artist.objects.filter(popularity__gt=80)

def task_2_artists_get_by_artistic_name():
    return Artist.objects.get(artistic_name='Jimi Hendrix')


def task_3_songs_delete():
    for song in Song.objects.all():
        if 't' in song.title.lower():
            song.delete()
    #Song.objects.filter(title__icontains='t').delete()
    
    
def task_4_artists_create_song():
    artist = Artist.objects.get(artistic_name = 'B.B. King')
    new_song = Song(artist_id=artist.id, title='Hello World', album_name='Python')
    new_song.save()
    #.create()
    
def task_5_artists_order_by_popularity():
    return Artist.objects.all().order_by('popularity')


def task_6_song_edit_album():
    song = Song.objects.get(title='Superstition')
    song.album_name = 'changed'
    song.save()
    
def task_7_song_counter():
    return len(Song.objects.all())
    #Song.objects.count()


