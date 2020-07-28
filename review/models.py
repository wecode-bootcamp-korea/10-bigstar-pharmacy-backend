from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=20)
    purchased_item = models.CharField(max_length=50)
    purchased_date = models.CharField(max_length=50)
    photo = models.CharField(max_length=200)
    comment = models.TextField()
    #user = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'reviews'
