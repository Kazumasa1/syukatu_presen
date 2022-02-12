import logging

from django.views import generic
from .forms import InquiryForm
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Kobo_info
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('haiku:inquiry')

class InquiryView(generic.FormView):
    template_name = "detail.html"
    form_class = InquiryForm
    success_url = reverse_lazy('haiku:detail')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class KoboInfoView(generic.ListView):
    model = Kobo_info

    template_name = 'index.html'

    def get_queryset(self):
        kobos = Kobo_info.objects.filter(user=self.request.user).order_by('-created_at')
        return kobos

