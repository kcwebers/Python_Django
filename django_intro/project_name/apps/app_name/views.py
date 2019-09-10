from django.shortcuts import render

# from django.shortcuts import render, HttpResponse
# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")

# from django.shortcuts import render	# notice the import!

def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "app_name/index.html", context)
