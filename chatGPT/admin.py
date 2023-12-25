from django.contrib import admin
from .models import ChatText, Story, Games

admin.site.register(Games)
admin.site.register(ChatText)
admin.site.register(Story)
