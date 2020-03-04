from django.shortcuts import render
from .models import SharePlace, Item
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage


import uuid

# Create your views here.
def index(request):
    if(request.GET):
        try:
            shareplace = SharePlace.objects.get(code=request.GET.get('code'))
        except Exception as e:
            return redirect(index)
        return display_shareplace(request, shareplace.code)

    return render(request, 'index.html')


def create_code():
    return uuid.uuid4().hex[:8].upper()

def create_shareplace(request):
    success = False
    while( not success ):
        try:
            shareplace = SharePlace(code=str(create_code()))
            success = True
        except:
            pass
    shareplace.save()
    return redirect(display_shareplace, code=shareplace.code)

def display_shareplace(request, code):
    if request.method == 'POST':
        item = Item(text=request.POST.get('textarea'), shareplace=SharePlace.objects.get(code = code))
        if (request.FILES):
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            item.file = uploaded_file_url

        item.save()
    items = Item.objects.filter(shareplace = SharePlace.objects.get(code = code))

    return render(request, 'shareplace.html', {'items':items, 'code':code})

def remove_shareplace(request, code):
    SharePlace.objects.get(code=code).delete()
    return redirect(index)

def remove_item(request, id):
    shareplace = Item.objects.get(pk=id).shareplace
    Item.objects.get(pk=id).delete()
    return display_shareplace(request, shareplace.code)

