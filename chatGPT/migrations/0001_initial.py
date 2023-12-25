# Generated by Django 4.2.8 on 2023-12-25 08:52

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
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
                ('role', models.CharField(max_length=20)),
                ('health', models.IntegerField(default=100)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=50)),
                ('health', models.IntegerField(default=100)),
                ('story', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatGPT.story')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChatText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_player', models.TextField(default='что то я не хочу отвечать ')),
                ('text', models.TextField()),
                ('games', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatGPT.games')),
            ],
        ),
    ]
