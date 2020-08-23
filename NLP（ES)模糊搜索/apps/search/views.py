from django.shortcuts import render
from django.views import View

from src.trainsport.city_qa_main import answer


class IndexView(View):
    def get(self, request):
        return render(request, 'home/home.html')

    def post(self, request, *args, **kwargs):
        question = request.POST.get('question', '')
        if question:
            result = answer(question)
        return render(request, 'home/home.html', context={"result": result, "question": question})


