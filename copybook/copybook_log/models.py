from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    slug = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.slug


class Summary(models.Model):
    """Информация записанная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    full_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'summarys'

    def __str__(self):
        """Возвращает строковое представление модели"""
        if self.full_text <= self.full_text[:50]:
            return f'{self.heading} \n{self.full_text}'
        else:
            return f'{self.heading} \n{self.full_text[:50]}...'
