from django.urls import path
from posts.views import PostList, PostDetail

#Urls here
urlpatterns = [
    #with build in classes [ListCreateAPIView and RetrieveUpdateDeleteAPIView]
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]