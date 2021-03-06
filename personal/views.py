from .models import Image
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt


# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')


# def image_of_day(request):
#     date = dt.date.today()
#     return render(request, 'make-images/today-image.html', {"date":date,})


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
# View Function to present image from past days
def past_days_image(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()


    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(image_of_day)

    photos = Image.days_image(date) 
    return render (request, 'make-images/past-image.html', {"date":date,"image":image})


def image_today(request):
    date = dt.date.today()
    image= Image.todays_image()
    return render(request, 'make-images/today-image.html', {"date": date,"image":image})



def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'make-images/search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'make-images/search.html',{"message":message})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ValueError:
        raise Http404()
    return render(request,"make-images/image.html", {"image":image})