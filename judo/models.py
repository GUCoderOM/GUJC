from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True)
    slug = models.SlugField(unique = True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    name = models.CharField(max_length=128, unique=False)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    picture = models.ImageField(upload_to='item_images', blank=True)

    class Meta:
        verbose_name_plural = 'Items'

    def save(self, *args, **kwargs):
        if not self.id:
            # Assuming you want to generate a slug based on the item's name
            self.slug = slugify(self.name)

        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question