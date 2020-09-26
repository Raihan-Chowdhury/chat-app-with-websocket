from django.shortcuts import render
from .models import msg

# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    # print("f")
    # if request.method == 'POST':
    #     print("f2")
    #     vl = request.POST['vl']
    #     vl += 1
    #     Msg = msg.objects.all().order_by('-timestamp')[:vl]
    #     print("f3")
    #     return render(request, 'chat/chatroom.html', {
    #         'room_name': room_name,
    #         'Msg': Msg,
    #         'vl' : vl
    #     })

    if (room_name == 'Marsteo'):
        Msg = msg.objects.all().order_by('-timestamp')[:200]
        return render(request, 'chat/chatroom.html', {
            'room_name': room_name,
            'Msg': Msg,
        })