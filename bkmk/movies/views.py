from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Movie
from reviews.models import Review
# from .forms import GenreForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

# Create your views here.


MY_API_KEY = '3216cd88663607c5472c0d1e54a7193a' # 환경변수로 만들어야 함

@login_required
def main(request):
    user = request.user
    usergenre = user.usergenre
    usergenre_list = list(usergenre[1:-1].split(', '))

    order = "Movie.objects.filter("
    for genre_id in usergenre_list:
        ID = genre_id[1:-1]
        order += f"Q(genres=int({ID}))|"
    order = order[:-1] + ')'
    if order == 'Movie.objects.filter(':
        raise Exception
    num = random.randint(1, 20)
    recommend_movie = eval(order+'[num-1:num]')
    r_reviews = Review.objects.filter(movie=recommend_movie)
    count=numsum=0
    for review in r_reviews:
        numsum += review.star_point
        count+=1
    average = 0
    if count:
        average = int(numsum/count)
    average_point=[]
    for i in range(average):
        average_point.append(i)

    movies = Movie.objects.all()
    paginator = Paginator(movies, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user':user,
        'movies': movies,
        'page_obj': page_obj,
        'recommend_movie':recommend_movie[0],
        'average_point':average_point,
    }
    return render(request, 'movies/main.html', context)

@login_required
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = Review.objects.filter(movie_id=movie.pk)
    popularity = int(movie.popularity)

    r_reviews = Review.objects.filter(movie=movie)
    count=numsum=0
    for review in r_reviews:
        numsum += review.star_point
        count+=1
    average = 0
    if count:
        average = int(numsum/count)
    average_point=[]
    for i in range(average):
        average_point.append(i)

    context = {
        'movie': movie,
        'popularity':popularity,
        'reviews':reviews,
        'average_point':average_point,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def genre_list(request, genre_pk):
    genre_choice = get_object_or_404(Genre, pk=genre_pk)
    movies = Movie.objects.filter(genres=genre_choice.pk).order_by('-vote_average')
    genres = Genre.objects.all()
    paginator = Paginator(movies, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'genre_choice':genre_choice,
        'movies':movies,
        'page_obj':page_obj,
    }
    return render(request, 'movies/genre_list.html', context)

@login_required
def recommend(request):
    user = request.user
    usergenre = user.usergenre
    usergenre_list = list(usergenre[1:-1].split(', '))

    order = "Movie.objects.filter("
    for genre_id in usergenre_list:
        ID = genre_id[1:-1]
        order += f"Q(genres=int({ID}))|"
    order = order[:-1] + ')'
    if order == 'Movie.objects.filter(':
        raise Exception
    recommend_movies = eval(order+".order_by('-vote_average')")
    paginator = Paginator(recommend_movies, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user':user,
        'recommend_movies': recommend_movies,
        'page_obj': page_obj,
    }
    return render(request, 'movies/recommend.html', context)