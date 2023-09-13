brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Brand name')
    logo = models.ImageField(upload_to='media/images', blank=True, null=True, verbose_name='Image')

    def __str__(self):
        return self.name