from django.urls import path
from .views import ChatMasterView, StoryView, ChatTextList, GamesDetailView

urlpatterns = [
    path('story/', StoryView.as_view(), name='story'),
    path('all-games/', ChatTextList.as_view(), name='user-update'),
    path('game/<int:pk>/events/', ChatMasterView.as_view(), name='game-events'),
    path('games/<int:pk>/', GamesDetailView.as_view(), name='games-detail'),
]