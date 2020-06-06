from django.conf import settings
from django.db import models
from django.utils import timezone


STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to="static/img/", null=True)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.status = 1
        self.save()

    def __str__(self):
        return self.title
