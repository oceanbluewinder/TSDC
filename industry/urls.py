from django.urls import path, include
from industry import views

app_name = "industry"
urlpatterns = [
    path('aboutus1',views.aboutus1,name='aboutus1'),

    path('question1',views.question1,name='question1'),
    path('question2',views.question2,name='question2'),
    path('question3',views.question3,name='question3'),
]

