from django.db import models

# Create your models here.
<<<<<<< HEAD
class FeedbackContacts(models.Model):
    full_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=200, default="")
    phone_number = models.CharField(max_length=10, default="")
    subject = models.CharField(max_length=200, default="")
    message = models.CharField(max_length=500, default="")
=======
class FeedbackContact (models.Model):
    full_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
>>>>>>> aa49e4dccf4389b93585de855901ae7a5d1f2dcf
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(FeedbackContact, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name + ' -  ' + self.subject
