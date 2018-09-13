from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here

class Song(models.Model):
    song_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    text = models.TextField()
    link = models.URLField() #default max is 200
    users_who_played_this_song = models.ManyToManyField(get_user_model(), through='Played_Song')
    distance_to_other_songs = models.ManyToManyField("self", through='Distance', symmetrical=False)
    #nearby_users = models.ManyToManyField(get_user_model(), through='Distance_to_User') #later add to user when customizing user model


    def __str__(self):
        song = self.artist + '-' + self.song_name
        return song

    def get_absolute_url(self):
        return reverse('song-detail', args=[str(self.id)])

class List(models.Model):
    name = models.CharField(max_length=100, default='My_List')
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, through='Song_in_list', related_name = 'songs_in_list')
    nearby_songs = models.ManyToManyField(Song, through='Distance_to_List', related_name = 'nearby_songs')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-detail', args=[str(self.id)])
        
class Song_in_List(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return self.song_id.name

    def get_absolute_url(self):
        return reverse('song-detail', args=[str(self.song_id.id)])




class Played_Song(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    numOfTimesPlayed = models.PositiveIntegerField(default=1) #esi neco nebude fungovat tak je to tady
    OPINION_CHOICES = (
            (1, 'Like'),
            (0, 'No opinion'),
            (2, 'Dislike'),
    )
    opinion = models.IntegerField(choices=OPINION_CHOICES, default=0)

    def get_absolute_url(self):
        return reverse('song-detail', args=[str(self.song_id.id)])


class Distance(models.Model):
    songs = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    distance = models.FloatField(default=0)
    DISTANCE_CHOICES = (
            ('TF-idf','TF-idf'),
            ('W2V', 'Word2Vec')
    )
    distance_Type = models.CharField(max_length=20, choices=DISTANCE_CHOICES)


class Distance_to_List(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, null=True)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    distance = models.FloatField()
    DISTANCE_CHOICES = (
            ('TF-idf', 'TF-idf'),
            ('W2V', 'Word2Vec')
    )
    distance_Type = models.CharField(max_length= 20, choices=DISTANCE_CHOICES)

    def get_nearby_songs(listid):
       nearby_songs = Distance_to_List.objects.filter(list_id=listid).order_by('-distance')[:10]
       return nearby_songs
    

class Distance_to_User(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    distance = models.FloatField(default=0)
    DISTANCE_CHOICES = (
            ('TF-idf', 'TF-idf'),
            ('W2V', 'Word2Vec')
    )
    distance_Type = models.CharField(max_length= 20, choices=DISTANCE_CHOICES, default='TF-idf')

    def get_nearby_songs(userid):
       nearby_songs = Distance_to_User.objects.filter(user_id=userid).order_by('-distance')[:10]
       return nearby_songs
