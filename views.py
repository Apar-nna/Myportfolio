from django.shortcuts import render, redirect
from .models import Profile, PortfolioItem
from .forms import ProfileForm, PortfolioItemForm

def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profiles/view_profile.html', {'profile': profile})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})

def portfolio(request):
    portfolio_items = PortfolioItem.objects.filter(user=request.user)
    return render(request, 'profiles/portfolio.html', {'portfolio_items': portfolio_items})

def add_portfolio_item(request):
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio_item = form.save(commit=False)
            portfolio_item.user = request.user
            portfolio_item.save()
            return redirect('portfolio')
    else:
        form = PortfolioItemForm()
    return render(request, 'profiles/add_portfolio_item.html', {'form': form})

def project_showcase(request):
    portfolio_items = PortfolioItem.objects.filter(user=request.user)
    return render(request, 'profiles/project_showcase.html', {'portfolio_items': portfolio_items})
