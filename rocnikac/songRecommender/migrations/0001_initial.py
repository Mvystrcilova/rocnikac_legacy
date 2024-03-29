# Generated by Django 2.0.7 on 2018-09-13 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField(default=0)),
                ('distance_Type', models.CharField(choices=[('TF-idf', 'TF-idf'), ('W2V', 'Word2Vec')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Distance_to_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('distance_Type', models.CharField(choices=[('TF-idf', 'TF-idf'), ('W2V', 'Word2Vec')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Distance_to_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField(default=0)),
                ('distance_Type', models.CharField(choices=[('TF-idf', 'TF-idf'), ('W2V', 'Word2Vec')], default='TF-idf', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='My_List', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Played_Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numOfTimesPlayed', models.PositiveIntegerField(default=1)),
                ('opinion', models.IntegerField(choices=[(1, 'Like'), (0, 'No opinion'), (2, 'Dislike')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('link', models.URLField()),
                ('distance_to_other_songs', models.ManyToManyField(through='songRecommender.Distance', to='songRecommender.Song')),
                ('users_who_played_this_song', models.ManyToManyField(through='songRecommender.Played_Song', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song_in_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songRecommender.List')),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songRecommender.Song')),
            ],
            options={
                'ordering': ['-order'],
            },
        ),
        migrations.AddField(
            model_name='played_song',
            name='song_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songRecommender.Song'),
        ),
        migrations.AddField(
            model_name='played_song',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='list',
            name='nearby_songs',
            field=models.ManyToManyField(related_name='nearby_songs', through='songRecommender.Distance_to_List', to='songRecommender.Song'),
        ),
        migrations.AddField(
            model_name='list',
            name='songs',
            field=models.ManyToManyField(related_name='songs_in_list', through='songRecommender.Song_in_List', to='songRecommender.Song'),
        ),
        migrations.AddField(
            model_name='list',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='distance_to_user',
            name='song_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='songRecommender.Song'),
        ),
        migrations.AddField(
            model_name='distance_to_user',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='distance_to_list',
            name='list_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='songRecommender.List'),
        ),
        migrations.AddField(
            model_name='distance_to_list',
            name='song_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='songRecommender.Song'),
        ),
        migrations.AddField(
            model_name='distance',
            name='songs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='songRecommender.Song'),
        ),
    ]
