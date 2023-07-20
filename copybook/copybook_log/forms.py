from django import forms

from .models import Topic, Summary


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['slug']
        labels = {'slug': ''}


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['heading', 'full_text']
        labels = {'full_text': '', 'heading': ''}
        widgets = {'full_text': forms.Textarea(attrs={'cols': 80})}
