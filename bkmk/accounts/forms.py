from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

USER_GENRE_CHOICES = (
    (28, '액션'),
    (16, '애니메이션'),
    (99, '다큐멘터리'),
    (18, '드라마'),
    (10751, '가족'),
    (14, '판타지'),
    (36, '역사'),
    (35, '코메디'),
    (10752, '전쟁'),
    (80, '범죄'),
    (10402, '음악'),
    (9648, '미스터리'),
    (10749, '로맨스'),
    (878, 'SF'),
    (27, '호러'),
    (10770, 'TV영화'),
    (53, '스릴러'),
    (37, '서부'),
    (12, '모험'),
)

class CustomUserChangeForm(UserChangeForm):
    usergenre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=USER_GENRE_CHOICES)
    class Meta:
        model = get_user_model()
        exclude = ['password']
        fields = ['username', 'email', 'age', 'use_adult', 'usergenre']

class CustomUserCreationForm(UserCreationForm):
    usergenre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=USER_GENRE_CHOICES)
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'age', 'use_adult', 'usergenre']
