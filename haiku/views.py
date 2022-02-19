import logging

import requests
from django.views import generic
# from .forms import InquiryForm
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SaitenForm
from django.shortcuts import render

from .models import Kobo_info


from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    kobo_list = Kobo_info.objects.all()
    return render(request, 'index.html', {'kobo_list': kobo_list})


class IndexView(generic.TemplateView):
    template_name = "index.html"




# class InquiryView(generic.FormView):
#     template_name = "inquiry.html"
#     form_class = InquiryForm
#     success_url = reverse_lazy('haiku:inquiry')


class DetailView(generic.DetailView, generic.FormView):
# class DetailView(generic.FormView):
    model = Kobo_info
    template_name = "detail.html"

    form_class = SaitenForm

    # 俳句採点formでsubmitボタンを押した時にリダイレクトさせるようにする
    def get_success_url(self):
        self.request.session['haiku'] = self.POST.get('haiku')
        return reverse('haiku:detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        # self.request.session['haiku'] = 'ssss'
        return super(DetailView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.request.session['haiku'] = self.request.POST.get('haiku')
        return self.get(request, *args, **kwargs)

    # def post_test(request):

    #     context = {
    #         'haiku': "POST method OK!!",
    #     }
    #     return render(request, 'detail.html', context)

    # def haiku(self, request):
    #     print(request.POST.get("haiku"))
    #     return super().haiku(request)

    # def form_valid(self, form):
    #     form.send_email()
    #     messages.success(self.request, 'メッセージを送信しました。')
    #     logger.info('inquiry sent by {}'.format(form.cleaned_data['name']))
    #     return super().form_valid(form)


# def form(request):
#     text = request.POST['haiku']
#     d = {
#         'message': 'POST!',
#         'text': text,
#     }
#     return render(request, 'detail.html', d)

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