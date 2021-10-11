from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


def home(request):
    rooms = Room.objects.all()
    # return HttpResponse('Home page')
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    # return HttpResponse('ROOM')
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
