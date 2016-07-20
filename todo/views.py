from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import addToList
from django.template import loader


def index(request):
    completeList = addToList.objects.all()
    context = {'completeList':completeList,}
    return render(request, 'todo/index.html', context)


def add(request):
    text=''
    if request.POST.get('input'):
        text = request.POST['input']
    list1 = addToList(list_text=text)
    list1.save()
    return HttpResponseRedirect('/todo/')


def completed(request):
    values = request.POST.getlist('checks[]')
    array = []
    for i in values:
        array.append(int(i) - 1)
    completelist = addToList.objects.all()
    if request.POST:
        if 'markasdone' in request.POST:
            count = 0
            for i in completelist:
                if len(array) > 0:
                    val = array[0]
                else:
                    break
                if count == val:
                    i.is_completed = True
                    i.save()
                    array.remove(val)
                count += 1

        elif 'Delete Selected' in request.POST:
            size = len(array)
            array.sort(reverse=True)
            for i in range(size):
                completelist[array[i]].delete()
        return HttpResponseRedirect('/todo/')