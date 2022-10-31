from http.client import HTTPResponse
from django.shortcuts import render, redirect
from . import models
from django.views import View
from .forms import TextForm


# 表示の際はformを使わないことにする
class IndexView(View):
    # 表示
    def get(self, request, *args, **kwargs):
        texts = models.Text.objects.all()
        context = {
            'texts' : texts,
        }
        return render(request, "home/index.html", context)
    # post受取り
    def post(self, request, *args, **kwargs):
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
