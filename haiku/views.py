import logging

from django.views import generic
from .forms import InquiryForm
# from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('haiku:inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)