from django.shortcuts import render

from .utils import get_turn_info

# Create your views here.


def peer1(request):
    # get numb turn info
    context = get_turn_info()

    return render(request, "core/peer1.html", context=context)


def peer2(request):
    # get numb turn info
    context = get_turn_info()

    return render(request, "core/peer2.html", context=context)


def peer(request):
    # get numb turn info
    context = get_turn_info()
    print("context: ", context)

    return render(request, "core/peer.html", context=context)
