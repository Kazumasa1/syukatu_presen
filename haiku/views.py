import logging
import environ
import requests
from django.views import generic
# from .forms import InquiryForm
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SaitenForm
from django.shortcuts import render

from .models import Kobo_info
from .models import Saiten_info

from bs4 import BeautifulSoup

from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.shortcuts import render

# Create your views here.

# .envファイルを読み込み
env = environ.Env()
env.read_env('.env')
# .envファイルからSECRET_KEYを読み込み
API_KEY = env('API_KEY')

logger = logging.getLogger(__name__)

def index(request):
    kobo_list = Kobo_info.objects.all()
    # sessionに保存された俳句をクリア
    request.session.clear()
    return render(request, 'index.html', {'kobo_list': kobo_list})


class IndexView(generic.TemplateView):
    template_name = "index.html"




# class InquiryView(generic.FormView):
#     template_name = "inquiry.html"
#     form_class = InquiryForm
#     success_url = reverse_lazy('haiku:inquiry')
SENTENCE = ""
url = "https://jlp.yahooapis.jp/MAService/V1/parse"
# params = {
#     "appid": API_KEY,
#     "sentence": SENTENCE,
#     # "sentence": "風に火をつける女の片えくぼ",
#     "response": "pos",
# }

class DetailView(generic.DetailView, generic.FormView):
# class DetailView(generic.FormView):
#     model = Saiten_info
    model = Kobo_info
    template_name = "detail.html"

    form_class = SaitenForm


    def post(self, request, *args, **kwargs):
        # self.request.session['haiku'] = self.request.POST.get('haiku')

        SENTENCE = self.request.POST.get('haiku')
        SENTENCE = SENTENCE.strip()
        SENTENCE = SENTENCE.replace(' ', '')
        SENTENCE = SENTENCE.replace('　', '')
        params = {
            "appid": API_KEY,
            "sentence": SENTENCE,
            "response": "pos",
        }
        res = requests.get(url, params=params)
        soup = BeautifulSoup(res.text, 'html.parser')
        word = soup.find_all('pos')
        pos_text = ""
        for text in range(len(word)):
            pos_text += word[text].text



        # 入力された俳句が採点モデルに存在するか？
        if Saiten_info.objects.filter(pos=pos_text).exists():
            pos = Saiten_info.objects.get(pos=pos_text)
            if 20 < pos.winningCount:
                self.request.session['comment'] = "素晴らしい作品ですね！！！"
            elif 15 < pos.winningCount and pos.winningCount < 20:
                self.request.session['comment'] = "とても良い作品ですね！"
            elif 10 < pos.winningCount and pos.winningCount < 15:
                self.request.session['comment'] = "すてきな作品ですね！"
            elif 3 < pos.winningCount and pos.winningCount < 10:
                self.request.session['comment'] = "まあまあの作品ですね"
            elif 0 < pos.winningCount and pos.winningCount < 3:
                self.request.session['comment'] = "まずまずの作品ですね"
            else:
                self.request.session['comment'] = "とても個性的な作品ですね"
        else:
            self.request.session['comment'] = "個性的な作品ですね"

        self.request.session['haiku'] = self.request.POST.get('haiku')
        # self.request.session['haiku'] = pos_text
        return self.get(request, *args, **kwargs)

    # 俳句採点formでsubmitボタンを押した時にリダイレクトさせるようにする
    def get_success_url(self):
        self.request.session['haiku'] = self.POST.get('haiku')
        return reverse('haiku:detail', kwargs={'pk': self.kwargs['pk']})



class KoboListView(generic.ListView):
    model = Kobo_info

    template_name = 'index.html'

    def get_queryset(self):
        kobos = Kobo_info.objects.all()

        cxt = {
            'kobo_list': kobos
        }

        return cxt


# def KoboListView(request):
#
#     kobo_list = Kobo_info.objects.all()
#     contest = {
#         'kobo_list': kobo_list,
#     }
#     return render(request, 'index.html', contest)

def list(request):
    data = Kobo_info.objects.all()
    params = {
        'data': data
    }
    return render(request, 'index.html', params)