from django.http import Http404
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import ChatText, Story, Games
from openai import OpenAI
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ChatGptSerializer, StorySerializer, ChatTextInfo, GamesSerializer

client = OpenAI(
    api_key="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",
)


class ChatTextList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = ChatText.objects.all()
    serializer_class = ChatTextInfo


class ChatMasterView(APIView):
    serializer_class = ChatGptSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user

        serializer = ChatGptSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        response_data = serializer.save()

        return Response(response_data, status=status.HTTP_200_OK)


class StoryView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StorySerializer

    def post(self, request, *args, **kwargs):
        user = request.user

        request_data = request.data.copy()
        request_data['user'] = user.id
        serializer = self.serializer_class(data=request_data)

        if serializer.is_valid():
            story = serializer.save(user=user)
            Games.objects.create(user=user, story=story, game_name=f"Game for {story.name}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user = request.user
        stories = Story.objects.filter(user=user)
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GamesDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Games.objects.get(pk=pk)
        except Games.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = GamesSerializer(game)
        return Response(serializer.data)