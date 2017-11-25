from django.shortcuts import render
from django.utils import timezone
from .models import Post

def home(request):
    books = Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')
    recent_review = books.first()
    past_books = books[1:]
    return render(request, 'bookblog/home.html', {'past_books': past_books, 'recent_review': recent_review})
