from django.shortcuts import render, redirect
from .models import Topic, Summary
from .forms import TopicForm, SummaryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def home_page(request):
    """Домашняя страница приложения Copybook"""
    return render(request, 'copybook_log/home_page.html')


@login_required
def topics_page(request):
    """Вывод списка тем"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'copybook_log/topics_page.html', context)


@login_required
def article_page(request, topic_id):
    """Выводит одну тему и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    # Проверка того, что одна тема принадлежит одному пользователю
    if topic.owner != request.user:
        raise Http404
    summarys = topic.summary_set.order_by('-date_added')
    contex = {'topic': topic, 'summarys': summarys}
    return render(request, 'copybook_log/article_page.html', contex)


@login_required
def new_topic_page(request):
    """Определяет новую тему"""
    if request.method != 'POST':
        # Данные не отправились; создается пустая форма
        form = TopicForm()
    else:
        # Отправленные данные POST; обработать данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_article_page = form.save(commit=False)
            new_article_page.owner = request.user
            new_article_page.save()
            return redirect('copybook_log:topics_page')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'copybook_log/new_topic_page.html', context)


@login_required
def new_article_page(request, topic_id):
    """Добавляет новую запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Данные не отправились, создается пустая форма
        form = SummaryForm()
    else:
        # Отправлены данные POST; обработать данные
        form = SummaryForm(data=request.POST)
        if form.is_valid():
            new_article_page = form.save(commit=False)
            new_article_page.topic = topic
            new_article_page.save()
            return redirect('copybook_log:article_page', topic_id=topic_id)
    # Вывести пустую или недействительную форму
    contex = {'topic': topic, 'form': form}
    return render(request, 'copybook_log/new_article_page.html', contex)


@login_required
def edit_article_page(request, summary_id):
    """Редактирует существующую запись"""
    summary = Summary.objects.get(id=summary_id)
    topic = summary.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = SummaryForm(instance=summary)
    else:
        form = SummaryForm(instance=summary, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('copybook_log:article_page', topic_id=topic.id)

    contex = {'summary': summary, 'topic': topic, 'form':form}
    return render(request, 'copybook_log/edit_article_page.html', contex)