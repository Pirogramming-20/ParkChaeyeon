from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def movies_list(request):
    review=Reviews.objects.all()
    context={
        "reviews" : review
    }
    print(review)

    return render(request, "movies_list.html",context)

def movies_read(request,pk):
    review=Reviews.objects.get(id=pk)
    context={
        "reviews" : review
    }
    return render(request,'movies_read.html',context)

def movies_create(request):
    if request.method=='POST':
        Reviews.objects.create(
            title=request.POST['title'],
            year=request.POST['year'],
            content=request.POST['content'],
        )
        return redirect("/reviews")
    return render(request,"movies_create.html")

def movies_update(request,pk):
    review=Reviews.objects.get(id=pk)
    if request.method =="POST":
        review.title=request.POST["title"]
        review.year=request.POST["year"]
        review.content=request.POST["content"]
        review.save()
        return redirect(f"/reviews/{pk}")
   
    context={
        "review":review
    }
    return render(request,"movies_update.html",context) 


def movies_delete(request,pk):
    if request.method =="POST":
        review=Reviews.objects.get(id=pk)
        review.delete()
    return redirect("/reviews")
