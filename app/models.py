from django.db import models

# Create your models here.

class FeedbackContact (models.Model):
    full_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(FeedbackContact, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name + ' -  ' + self.subject
