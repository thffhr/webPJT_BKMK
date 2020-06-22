from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Review
from .forms import ReviewCreateForm, ReviewUpdateForm
from movies.models import Movie


# Movie = Review.movie
@login_required
def reviewlist(request):
    reviews = Review.objects.all()
    top_reviews = Review.objects.order_by('-like_users')[:3] #인기 top3
    context = {
        'reviews':reviews,
        'top_reviews':top_reviews,
    }
    return render(request, 'reviews/reviewlist.html', context)

@login_required
def create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewCreateForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.movie = movie
                review.save()
                return redirect('reviews:detail', review.pk)
        else:
            form = ReviewCreateForm()
        context = {
            'form':form
        }
        return render(request, 'reviews/form.html', context)
    else:
        messages.warning(request, '로그인을 해주세요.')
        return redirect('accounts: login')

@login_required
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user.is_authenticated:
        if request.user == review.user:
            if request.method == "POST":
                form = ReviewUpdateForm(request.POST, instance=review)
                if form.is_valid():
                    updated_review = form.save(commit=False)
                    updated_review.user = request.user
                    updated_review.save()
                    return redirect('reviews:detail', review.pk)
            else:
                form = ReviewUpdateForm(instance=review)
            context = {
                'form':form
            }
            return render(request, 'reviews/form.html', context)
        else:
            messages.warning(request, '본인 글만 수정 가능합니다.')
            return redirect('reviews:detail', review.pk)
    else:
        messages.warning(request, '로그인을 해주세요')
        return redirect('accounts:login')



def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user.is_authenticated:
        if request.user == review.user:
            review.delete()
            return redirect('reviews:reviewlist')
        else:
            messages.warning(request, '본인 글만 수정 가능합니다.')
            return redirect('reviews:detail', review.pk)
    else:
        messages.warning(request, '로그인을 해주세요')
        return redirect('accounts:login')

def detail(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    movie = review.movie
    context = {
        'movie': movie,
        'review': review,
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def like(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    # if request.user != review.user:
    if review.like_users.filter(id=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('reviews:detail', review.pk)