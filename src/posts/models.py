from django.db import models

# Create your models here.

class PostModel(models.Model):

    title       = models.CharField(max_length=127)
    content     = models.TextField()
    available   = models.BooleanField(default=True)
    price       = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

    @property
    def images(self):
        instance = self
        print(self.id)
        qs = ImageModel.objects.filter(post=self).first()
        print(qs.image.url)
        return qs



class ImageModel(models.Model):
    post        = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='images/', #upload_location,
                                    null=True,
                                    blank=True,
                                    height_field = 'height_field',
                                    width_field = 'width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}".format(self.post.title, self.id)
