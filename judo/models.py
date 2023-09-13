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
    item_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=128, unique=False)
    slug = models.SlugField(unique = True)
    quantity = models.IntegerField(blank=True,null=True)
    picture = models.ImageField(upload_to='item_images', blank=True)

    class Meta:
        verbose_name_plural = 'Items'

    def save(self, *args, **kwargs):
        if not self.id: # This ensures slug generation only happens on creation, not update
            # Get the related user's profile (assuming userprofile is the related_name in the User model)
            user_profile = self.item_user.userprofile

            # Combine the user's slug and the item's name to form the item's slug
            self.slug = slugify(f"{user_profile.slug}-{self.name}")

        super(Item, self).save(*args, **kwargs)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question