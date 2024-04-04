from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.urls import reverse
# Managers>>>
#https://docs.djangoproject.com/en/5.0/topics/db/managers/
class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)

# Create your models here.
class Post(models.Model):
    #https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    # Choice Fields>>>
    class Status(models.TextChoices):
        PUBLISHED = 'PB' , 'Published'  
        DRAFT = 'DF' , 'Draft'
        REJECTED = 'RJ' , 'Rejected'
    
    # Relations(many to one)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts", verbose_name='نویسنده')
    #https://docs.djangoproject.com/en/5.0/ref/models/fields/
    # Data Fields>>>
    title = models.CharField(max_length=250,verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(max_length=250)
    # Date Fields>>>
    publish = jmodels.jDateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    # Choice Fields>>>
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT,verbose_name='وضعیت')
    
    #objects = models.Manager()
    objects = jmodels.jManager()
    published = PublishedManager()
    #https://docs.djangoproject.com/en/5.0/ref/models/options/
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
        #فارسی سازی پنل ادمین جنگو>>> verbose_name=''
        verbose_name_plural= 'پست ها'
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])
    
