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
    itemPrice = models.IntegerField()
    picture = models.ImageField(upload_to='item_images', blank=True)
    stripe_product_id = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Items'

    def save(self, *args, **kwargs):
        if not self.id:
            # Assuming you want to generate a slug based on the item's name
            self.slug = slugify(self.name)

        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    id = models.CharField(primary_key=True,max_length=100)
    price = models.IntegerField(default = 60)
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question