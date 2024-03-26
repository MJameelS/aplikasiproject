from django.shortcuts import render
from .models import Products
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm



def landing(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Products.objects.all()
    return render(request, "index.html", context)

def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Products.objects.get(id = id)
         
    return render(request, "product.html", context)

# def contact(request)

def contact(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Products.objects.all()
    return render(request, "contact.html", context)
    

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POTS)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("landing") 


# login page
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# signup page
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


