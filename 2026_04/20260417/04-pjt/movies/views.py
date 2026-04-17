import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def get_director_info(director_name):
    # 1. 위키피디아 API 호출 설정
    wiki_url = "https://ko.wikipedia.org/w/api.php"
    
    # [수정] 위키피디아는 요청자의 정보를 담은 User-Agent를 필수로 요구하는 경우가 많습니다.
    headers = {
        'User-Agent': 'MyMovieApp/1.0 (ssafy_student_project@example.com)'
    }
    
    wiki_params = {
        "action": "query",
        "format": "json",
        "prop": "extracts|pageimages",
        "titles": director_name,
        "exintro": True,
        "explaintext": True,
        "pithumbsize": 500,
    }
    
    try:
        # headers를 포함하여 요청을 보냅니다.
        response = requests.get(wiki_url, params=wiki_params, headers=headers, timeout=5)
        
        # 응답이 비어있는지 먼저 체크하여 에러를 방지합니다.
        if not response.text:
            return "", "위키백과 응답이 없습니다.", "정보 없음"
            
        wiki_res = response.json()
        pages = wiki_res.get('query', {}).get('pages', {})
        
        if not pages or "-1" in pages:
            wiki_text = "해당 감독에 대한 위키백과 정보가 없습니다."
            img_url = ""
        else:
            page = list(pages.values())[0]
            wiki_text = page.get('extract', '정보 없음')
            img_url = page.get('thumbnail', {}).get('source', '')

        # 2. Upstage API 호출 (성공했던 test.py 로직)
        api_key = "up_vezHFzV4l8jRZBwlwFDz5Nv7XKg6W"
        url = "https://api.upstage.ai/v1/solar/chat/completions"
        
        payload = {
            "model": "solar-1-mini-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that outputs only valid JSON."},
                {"role": "user", "content": f"감독 '{director_name}'의 정보를 JSON으로 요약해줘. 형식: {{\"director_info\": \"...\", \"director_works\": \"...\"}} 정보: {wiki_text}"}
            ],
            "response_format": {"type": "json_object"}
        }

        ai_response = requests.post(
            url, 
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}, 
            json=payload, 
            timeout=15
        )
        
        if ai_response.status_code == 200:
            ai_data = ai_response.json()
            raw_content = ai_data['choices'][0]['message']['content']
            cleaned_content = raw_content.strip().replace('```json', '').replace('```', '').strip()
            result = json.loads(cleaned_content)
            
            return img_url, result.get('director_info', ''), result.get('director_works', '')
        else:
            return img_url, "AI 요약 실패", "정보 없음"

    except Exception as e:
        # 터미널에서 어떤 단계가 문제인지 파악하기 위해 구체적인 에러를 찍어줍니다.
        print(f"!!! [ERROR] get_director_info 단계에서 예외 발생: {e}")
        return "", "정보를 불러오는 중 오류가 발생했습니다.", "정보 없음"

def create(request):
    if request.method == 'POST':
        print("1. POST 요청 들어옴")
        form = MovieForm(request.POST) 
        if form.is_valid():
            print("2. 유효성 검사 통과")
            movie = form.save(commit=False)
            
            # AI API 호출 전후 확인
            print("3. AI API 호출 시작 (시간이 걸릴 수 있음)")
            img_url, info, works = get_director_info(movie.director)
            print("4. AI API 호출 완료")
            
            movie.director_img_url = img_url
            movie.director_info = info
            movie.director_works = works
            
            movie.save()
            print("5. DB 저장 완료")
            return redirect('movies:detail', movie.pk)
        else:
            print("!! 유효성 검사 실패:", form.errors) # 에러 내용 터미널에 출력
    else:
        form = MovieForm() 
    
    context = { 'form': form }
    return render(request, 'movies/create.html', context)

# detail, index, update, delete 함수는 기존과 동일하게 유지
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)





def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    elif request.method == 'GET':
        form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')

    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)


def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        movie.delete()

    return redirect('movies:index')