from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from .forms import SignUpForm


def register(request):
    """Регистрация нового пользователя."""
    if request.method != 'POST':
        # Выводит пустую форму регистрации
        form = SignUpForm()
    else:
        # Обработка заполненной формы
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('copybook_log:home_page')

    # Вывести пустую форму
    contex = {'form': form}
    return render(request, 'registration/register.html', contex)

