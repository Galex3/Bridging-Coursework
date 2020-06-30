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
    image = models.ImageField(upload_to="static/img/", blank=True, null=True)
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

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": str(self.slug)})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


# Classes for TDD

class CVExperience(models.Model):
    role = models.TextField(default='')
    company = models.TextField(default='')
    duration = models.TextField(default='')
    item1 = models.TextField(default='')
    item2 = models.TextField(default='')
    item3 = models.TextField(default='')


class Education(models.Model):
    degree = models.TextField(default='')
    institution = models.TextField(default='')
    duration = models.TextField(default='')
    item1 = models.TextField(default='')
    item1_grade = models.DecimalField(default=40.00, max_digits=5, decimal_places=2)
    item2 = models.TextField(default='')
    item2_grade = models.DecimalField(default=40.00, max_digits=5, decimal_places=2)
    item3 = models.TextField(default='')
    item3_grade = models.DecimalField(default=40.00, max_digits=5, decimal_places=2)


class HardSkill(models.Model):
    icon = models.TextField(default='')


class SoftSkill(models.Model):
    text = models.TextField(default='')


class Project(models.Model):
    title = models.TextField(default='')
    description = models.TextField(default='')
    duration = models.TextField(default='')
    link = models.TextField(default='', blank=True)


class Interest(models.Model):
    icon = models.TextField(default='')


class Language(models.Model):
    name = models.TextField(default='')
    proficiency = models.TextField(default='')
    level = models.IntegerField(default=1)
