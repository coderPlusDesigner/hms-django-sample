from django.shortcuts import render, redirect
from .models import Link, Category
from .forms import LinkForm

def home(request):
    categories = Category.objects.all()
    category_slug = request.GET.get('category')
    
    links = Link.objects.select_related('category').order_by('-created_at')
    
    if category_slug:
        links = links.filter(category__slug=category_slug)
    
    return render(request, 'links/home.html', {
        'links': links,
        'categories': categories,
        'active_category': category_slug,
    })

def submit_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LinkForm()
    
    return render(request, 'links/submit.html', {'form': form})