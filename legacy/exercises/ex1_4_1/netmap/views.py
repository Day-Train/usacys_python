from django.shortcuts import render
from hashlib import sha1

# Create your views here.
def index(request):
    return render(request, 'netmap\index.html', {'digest': sha1('ex1_4_1').hexdigest()})