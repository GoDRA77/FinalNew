from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name='stories')  # Пользователь истории
    story_name = models.CharField(max_length=30, unique=True)  # Название истории
    description = models.TextField()  # Описание истории
    player_role = models.CharField(max_length=20)  # Роль игрока
    health = models.IntegerField(default=100)  # Здоровье игрока

    def __str__(self):
        return f"Player {self.pk}"


class Games(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name='games')  # Пользователь игры
    story = models.ForeignKey(Story, on_delete=models.CASCADE, default=1, related_name='games')  # История игры
    game_name = models.CharField(max_length=50)  # Название игры
    health = models.IntegerField(default=100)  # Здоровье игры

    def __str__(self):
        return f"Game #{self.pk}"


class ChatText(models.Model):
    answer_player = models.TextField(default='NONE')  # Ответ игрока в чате
    text = models.TextField()  # Текст сообщения в чате
    game = models.ForeignKey(Games, on_delete=models.CASCADE, default=1, related_name='chat_texts')  # Игра, к которой относится чат

    def __str__(self):
        return f"Chat Text #{self.pk}"
