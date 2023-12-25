from rest_framework import serializers
from Auth.models import CustomUser
from .models import ChatText, Story, Games


class ChatTextInfo(serializers.ModelSerializer):
    class Meta:
        model = ChatText
        fields = '__all__'


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['id', 'user', 'story', 'game_name', 'max_events']


class ChatGptSerializer(serializers.ModelSerializer):
    games = GamesSerializer(required=False)

    class Meta:
        model = ChatText
        fields = ['id', 'text', 'answer_player',  'games']

    def create(self, validated_data):
        user = self.context['request'].user
        input_text = validated_data['text']

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

        health_indexes = [response_text.find("Здоровье - "), response_text.find("Здоровье игрока:")]
        health_values = []

        for index in health_indexes:
            if index != -1:
                value = int(response_text[index + len("Здоровье - "):].split('.')[0].strip())
                health_values.append(value)

        if health_values:
            current_game.story.health = max(health_values)
            current_game.story.save()

        response_text = response_text.replace(f"Здоровье игрока: {current_game.story.health}", "")
        response_data = {"text": f"{response_text} Здоровье игрока: {current_game.story.health}"}

        return response_data

    def send_to_chatgpt(self, input_text, description):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"В конце ты должен описать что произойдет дальше..."
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


class StorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Story
        fields = ['id', 'name', 'role', 'description', 'health', 'user']