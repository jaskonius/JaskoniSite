from django.shortcuts import render

# Create your views here.
def root(request):
    return render(request, "spotify/root.html")
