from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def home(request):
    books = Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')
    recent_review = books.first()
    past_books = books[1:8]
    return render(request, 'bookblog/home.html', {'past_books': past_books, 'recent_review': recent_review})

def review_detail(request, pk):
    book_review = get_object_or_404(Post, pk=pk)
    return render(request, 'bookblog/review_detail.html', {'book_review': book_review})

def about(request):
    return render(request, 'bookblog/about.html', {})

def all_reviews(request):
    books = Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')
    return render(request, 'bookblog/allreviews.html', {'books': books})
