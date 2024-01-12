from django.shortcuts import render
from .models import*

# Create your views here.
def movies_list(request):
    reviews=Reviews.objects.all()
    context={
        "reviews" : reviews
    }
    print(reviews)

    return render(request, "movies_list.html",context)