from django.db import models
from .consts import MAX_RATE

RATE_CHOICES = [(x,str(x)) for x in range(0, MAX_RATE + 1)]

CATEGORY = (('サイエンスフィクション','SF'),('アクション','Action'),('ホラー','Horror'),
            ('ドキュメンタリー','Documentary'),('スリラー','thriller'),
            ('ドラマ','Drama'),('コメディ','Comedy'),('アドベンチャー','Adventure'),('その他','other')
            )
CATEGORY2 = (('邦画','japan'),('洋画','world'),('アニメ','anime'))


class Movie(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(
        max_length = 100,
        choices = CATEGORY
       
    )
    category2 = models.CharField(
        max_length = 100,
        choices = CATEGORY2
       
    ) 
    
        

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.
