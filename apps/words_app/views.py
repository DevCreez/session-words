from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(request):
    if "words" not in request.session:
        request.session["words"] = []
    return render(request, "words_app/index.html")

def process(request):
    word = {
        "word": request.POST["word"],
        "time": datetime.strftime(datetime.now(), "%H:%M:%S, %B %d %Y")
    }

    if "font" not in request.POST:
        word["fontsize"] = "small"
    else:
        word["fontsize"] = request.POST["font"]

    if "color" not in request.POST:
        word["color"] = "black"
    else:
        word["color"] = request.POST["color"]
    print word

    request.session["words"].append(word)
    request.session.modified = True
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")