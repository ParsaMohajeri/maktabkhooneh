from django.db import models

# Create your models here.
class Post(models.Model):
    # image=models.ImageField(upload_to='blog/',default='blog/defalt.jpg')
    # author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    # tags = TaggableManager()
    # category=models.ManyToManyField(Category)
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    # login_require=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('created_date',)
        # verbose_name='Post'
        # verbose_name_plural='Posts'

    def __str__(self):
        return " {} ".format(self.title)