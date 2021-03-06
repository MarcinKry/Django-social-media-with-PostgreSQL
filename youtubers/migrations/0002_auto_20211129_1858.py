# Generated by Django 3.2.9 on 2021-11-29 17:58

from django.db.models.fields import NullBooleanField
import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('canon', 'canon'), ('niko', 'niko'), ('sony', 'sony'), ('red', 'red'), ('other', 'other')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('code', 'code'), ('mobile_review', 'mobile_review'), ('vlogs', 'vlogs'), ('comedy', 'comedy'), ('film_making', 'film_making')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='city',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='youtuber',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='photo',
            field=models.ImageField(default='', upload_to='media/ytubers/%Y/%m/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='subs_count',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='video_url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
