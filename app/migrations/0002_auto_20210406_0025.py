# Generated by Django 3.1.7 on 2021-04-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackcontacts',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='feedbackcontacts',
            name='full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='feedbackcontacts',
            name='message',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='feedbackcontacts',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='feedbackcontacts',
            name='subject',
            field=models.CharField(default='', max_length=200),
        ),
    ]