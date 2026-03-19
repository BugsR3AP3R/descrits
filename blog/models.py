from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.TextChoices):
    CARNET = 'carnet', 'Carnet de Lecture'
    TEXTES = 'textes', 'Fiction & Confidences'
    PENSEES = 'pensees', 'Pensées en vrac'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.CARNET,
        verbose_name="Catégorie"
    )
    cover_image = models.ImageField(
        upload_to='covers/', blank=True, null=True,
        verbose_name="Image de couverture"
    )
    # For book summaries
    author_name = models.CharField(
        max_length=200, blank=True,
        verbose_name="Auteur du livre"
    )
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        blank=True, null=True,
        verbose_name="Note /5"
    )
    excerpt = models.TextField(
        max_length=400, blank=True,
        verbose_name="Extrait / Résumé court"
    )
    content = models.TextField(verbose_name="Contenu")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name="Publié")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_stars(self):
        return range(self.rating) if self.rating else []

    def get_empty_stars(self):
        return range(5 - self.rating) if self.rating else range(5)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    content = models.TextField(verbose_name="Commentaire")
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False, verbose_name="Approuvé")

    class Meta:
        ordering = ['created_at']
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return f"Commentaire de {self.name} sur {self.post.title}"
