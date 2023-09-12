from django.urls import path

from .views import CategoryListView, ProblemListView,ChoiceDetailView, results_view


app_name = 'compe'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('problem/<int:pk>/', ProblemListView.as_view(), name='problem'),
    path('choice/<int:pk>/', ChoiceDetailView.as_view(), name='choice_detail'),
    path('results/', results_view, name='results'),
]