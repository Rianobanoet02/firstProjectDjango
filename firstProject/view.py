from django.http import HttpResponse

# methot view index
def index(request):
    return HttpResponse("<h1> ini  adalah Home</h1>")

def about(request):
    return HttpResponse("<h1> ini  adalah About</h1>")