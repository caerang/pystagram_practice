from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy


# Create your models here.


class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(using, keep_parents)

    def get_absolute_rul(self):
        url = reverse_lazy('detail', kwargs={'pk': self.pk})
        return url
