from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import *
from Test.classify import analyse
import os

from WasteDetection.settings import BASE_DIR


def index(request):
    return render(request, 'index.html')


def test(request):

    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)

        if form.is_valid():
            test_obj = form.save(commit=False)
            test_obj.save()
            img_path = test_obj.img.url
            print(os.path.abspath(__file__))
            img_path = BASE_DIR + img_path

            test_result = analyse(img_path)
            print(test_result)
            return JsonResponse(test_result)
            # return render(request, 'success.html', test_result)
    else:
        form = TestForm()
    return render(request, 'test.html', {'form': form})


def success(request):
    return HttpResponse('Success')
