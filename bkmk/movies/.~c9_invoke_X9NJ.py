from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
# , Genre
# from .forms import GenreForm
import json
import requests

MY_API_KEY = '3216cd88663607c5472c0d1e54a7193a' # 환경변수로 만들어야 함

#######영화목록 저장########
def getmovieinfo(request):
    # admin이 아니면 들어오지 못하게 막아주기
    if request.user.is_superuser:
        # Genre
        # https://api.themoviedb.org/3/genre/movie/list?api_key={{  }}&language=en-US

        # 몇개나 가져오고 싶음? => n, m
        n = 2
        m = 3
        for page_num in range(n, m+1):
            MOVIE_LIST_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={MY_API_KEY}&language=ko-KR&page={page_num}"
            movie_list_data = requests.get(MOVIE_LIST_URL)
            movie_datas = movie_list_data.json().get('results')

            for data in movie_datas:
                movie_id = data.get('id')
                MOVIE_DETAIL_URL = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={MY_API_KEY}&language=ko-KR"
                movie_detail_data = requests.get(MOVIE_DETAIL_URL)

                director = actor = ''
                # 출연진
                CREDITS_URL = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={MY_API_KEY}"
                credits_data = requests.get(CREDITS_URL)
                crew_data = credits_data.json().get('crew')

                for n in range(5):
                    if crew_data[n].get('job') =='Director':
                        director = crew_data[n].get('name') # 영화감독 정보 저장
                        break
                    elif crew_data[n].get('job') =='Actor':
                        actor += ','
                        actor += crew_data[n].get('name') # 배우 정보 저장

                # 영화사
                company_data = movie_detail_data.json().get('production_companies')
                if company_data:
                    company = company_data[0].get('name')

                Movie.objects.get_or_create(
                    tmdb_id = movie_id,
                    title = data.get('title'),
                    backdrop_path = "https://image.tmdb.org/t/p/original" + data.get('backdrop_path'),
                    poster_path = "https://image.tmdb.org/t/p/original"+ data.get('poster_path'),
                    genre = movie_detail_data.json().get('genres')[0]['id'],
                    adult = movie_detail_data.json().get('adult'),
                    release_date = movie_detail_data.json().get('release_date'),
                    director = director,
                    runtime = movie_detail_data.json().get('runtime'),
                    production_company = company,
                    overview = movie_detail_data.json().get('overview'),
                    vote_average = movie_detail_data.json().get('vote_average'),
                    )

        movies = Movie.objects.all()
        context = {
            "movies":movies,
        }
        return render(request, 'movies/getmovieinfo.html', context)
    return redirect('movies:main')

def recommend(request):
    movies = Movie.objects.all()
    usergenre = request.user.usergenre

    if request.user.age >= 19:
        recommend_movies = Movie.objects.filter(genre=usergenre).order_by('-vote_average')
    else:
        recommend_movies = Movie.objects.filter(genre=usergenre, adult=False).order_by('-vote_average')

    comtext = {
        'recommend_movies':recommend_movies,
    }
    return render(request, 'movies/main.html', context)
