from django.urls import path
from categories.views import CategoriesView
from categories.views import CategoriesViewDetail

#Urls here
urlpatterns = [
    #with base class [APIView]
    path('', CategoriesView.as_view()),
    path('<int:pk>/', CategoriesViewDetail.as_view()),

]