from django.shortcuts import render


def index(request):
    return render(request, "index.html", {})


def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})
