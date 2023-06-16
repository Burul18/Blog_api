from django.urls import path
from category import views
from category.views import CategoryCreateListView, CategoryDetailView

urlpatterns = [
    path('', CategoryCreateListView.as_view()),
    path('<int:pk>/', CategoryDetailView.as_view()),
]