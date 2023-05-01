from django.urls import path
from . import views
urlpatterns=[
    path('hello/',views.f_view),
    path('hello2/<int:param>/',views.t_view),
    path('hello2/<int:param>/<int:year>/',views.t_view),
]