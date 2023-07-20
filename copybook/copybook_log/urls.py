"""Определяем схемы URL для copybook_log"""

from django.urls import path
from . import views

app_name = 'copybook_log'
urlpatterns = [
    # Домашняя страница
    path('', views.home_page, name='home_page'),
    # Страница со списком тем
    path('topics/', views.topics_page, name='topics_page'),
    # Страница с подробной информацией по отдельным темам
    path('topics/<int:topic_id>/', views.article_page, name='article_page'),
    # Страница для добавления новой темы пользователем
    path('new_topic_page/', views.new_topic_page, name='new_topic_page'),
    # Страница для добавления новой статьи пользователем
    path('new_article_page/<int:topic_id>/', views.new_article_page, name='new_article_page'),
    # Страница для редактирования записей
    path('edit_article/<int:summary_id>/', views.edit_article_page, name='edit_article_page'),
]
