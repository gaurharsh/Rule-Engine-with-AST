# rule_engine/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Home page
    path('create-rule/', views.create_rule_view, name='create_rule'),
    path('evaluate-rule/<int:rule_id>/', views.evaluate_rule_view, name='evaluate_rule'),
]
