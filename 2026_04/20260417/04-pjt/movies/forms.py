from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # fields = '__all__'  <-- 기존 코드가 있다면 지워주세요!
        
        # 사용자가 화면에서 직접 입력할 3가지 필수 항목만 지정합니다.
        fields = ('title', 'description', 'director',)