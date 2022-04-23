from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.views import *
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
from .models import *
from .utils import *

def get_movies_by_genre(genre_title):
    movie_list_in_this_genre = Movie.objects.filter(genre__title__exact=genre_title)
    return movie_list_in_this_genre


def glav(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    categories = Category.objects.all()
    films = Movie.objects.filter(category_id=1)
    context = {
        'movie_list': movies,
        'genre_list': genres,
        'cate_list' : categories,
        'films' : films,

    }
    return render(request,'main/ekran.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        # mail = EmailMessage(
        #     'Verify email',
        #     'Please, verify the your account',
        #     settings.EMAIL_HOST_USER,
        #     to=[form.cleaned_data.get('email')]
        # )
        # mail.send()
        #
        # if mail:
        user = form.save()
        login(self.request, user)
        return redirect('/')
        # else:
        # return redirect('register')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def movie_view(request, movie_id):
    current_movie = Movie.objects.get(pk=movie_id)
    context = {
        'movie': current_movie
    }

    return render(request,'main/details.html', context=context)
