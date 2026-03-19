from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Comment, Category


def home(request):
    recent_posts = Post.objects.filter(published=True)[:6]
    carnet_posts = Post.objects.filter(published=True, category=Category.CARNET)[:3]
    textes_posts = Post.objects.filter(published=True, category=Category.TEXTES)[:3]
    pensees_posts = Post.objects.filter(published=True, category=Category.PENSEES)[:3]
    context = {
        'recent_posts': recent_posts,
        'carnet_posts': carnet_posts,
        'textes_posts': textes_posts,
        'pensees_posts': pensees_posts,
    }
    return render(request, 'blog/home.html', context)


def carnet(request):
    posts = Post.objects.filter(published=True, category=Category.CARNET)
    return render(request, 'blog/category.html', {
        'posts': posts,
        'category_name': 'Carnet de Lecture',
        'category_desc': 'Entre les pages lues, des impressions, des émotions, des mots qui restent.',
        'category_icon': '📖',
        'category_slug': 'carnet',
    })


def textes(request):
    posts = Post.objects.filter(published=True, category=Category.TEXTES)
    return render(request, 'blog/category.html', {
        'posts': posts,
        'category_name': 'Fiction & Confidences',
        'category_desc': 'Des textes écrits à cœur ouvert — entre imaginaire et vérité.',
        'category_icon': '✍️',
        'category_slug': 'textes',
    })


def pensees(request):
    posts = Post.objects.filter(published=True, category=Category.PENSEES)
    return render(request, 'blog/category.html', {
        'posts': posts,
        'category_name': 'Pensées en vrac',
        'category_desc': 'Des réflexions qui ne demandent qu\'à être partagées.',
        'category_icon': '💭',
        'category_slug': 'pensees',
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    comments = post.comments.filter(approved=True)
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        content = request.POST.get('content', '').strip()
        if name and email and content:
            Comment.objects.create(post=post, name=name, email=email, content=content)
            messages.success(request, 'Votre commentaire a été soumis et sera visible après modération. Merci ! ✨')
            return redirect('post_detail', slug=slug)
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
    })


def about(request):
    return render(request, 'blog/about.html')
