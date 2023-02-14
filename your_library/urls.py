from django.urls import path
from . import views

app_name = 'your_library'
urlpatterns = [
    path('', views.IndexView.as_view(), name='your_library'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:post_id>/vote/', views.vote, name='vote'),
] 