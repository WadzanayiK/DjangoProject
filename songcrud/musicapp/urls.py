from django.urls import path

from . import views




from .views import ArtisteView
from .views import SongView
from .views import LyricView
from django.urls import path  
  
urlpatterns = [  
    path('api/', ArtisteView.as_view()),
    path('api/', SongView.as_view()),
    path('api/', LyricView.as_view())
]  