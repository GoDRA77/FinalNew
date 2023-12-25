from rest_framework import serializers
from Auth.models import CustomUser
from .models import ChatText, Story, Games
from openai import Client
client = Client(api_key="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")
# Создание сериализатора для модели ChatText


class ChatTextInfo(serializers.ModelSerializer):
    class Meta:
        model = ChatText
        fields = '__all__'
# Создание сериализатора для модели Games


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['id', 'user', 'story', 'game_name', 'max_events']
# Создание сериализатора для модели ChatText, который будет взаимодействовать с API OpenAI GPT-3.5


class ChatGptSerializer(serializers.ModelSerializer):
    games = GamesSerializer(required=False)

    class Meta:
        model = ChatText
        fields = ['id', 'text', 'answer_player', 'games']

    # Метод create, который создает новые объекты ChatText
    def create(self, validated_data):
        user = self.context['request'].user
        input_text = validated_data['text']
        # Поиск или создание новой игры (Games) и связанных объектов
        try:
            current_game = Games.objects.get(user=user, story__name=input_text)
        except Games.DoesNotExist:
            current_story = Story.objects.get(name=input_text)
            current_game = Games.objects.create(user=user, story=current_story, game_name=f"Game for {input_text}")

        validated_data['user'] = user
        validated_data['story'] = current_game.story
        validated_data['games'] = current_game

        response_text = self.send_to_chatgpt(input_text, current_game.story.description)
        ChatText.objects.create(text=input_text, answer_player=response_text, story=current_game.story, games=current_game)

        health_indexes = [response_text.find("Health - "), response_text.find("Player's health:")]
        health_values = []

        for index in health_indexes:
            if index != -1:
                value = int(response_text[index + len("Health - "):].split('.')[0].strip())
                health_values.append(value)

        if health_values:
            current_game.story.health = max(health_values)
            current_game.story.save()

        response_text = response_text.replace(f"Player's health: {current_game.story.health}", "")
        response_data = {"text": f"{response_text} Player's health: {current_game.story.health}"}

        return response_data

    # Метод для отправки текста пользовательского ввода в OpenAI для генерации ответа
    def send_to_chatgpt(self, input_text, description):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"At the end, you should describe what will happen next..."
                },
                {
                    "role": "assistant",
                    "content": f"  {description}."
                },
                {
                    "role": "user",
                    "content": input_text,
                }
            ],
            model="gpt-3.5-turbo",
            temperature=1,
            max_tokens=500
        )

        return chat_completion.choices[0].message.content
# Создание сериализатора для модели Story


class StorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Story
        fields = ['id', 'name', 'role', 'description', 'health', 'user']
