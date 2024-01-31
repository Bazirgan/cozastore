from django.db import models

SIZE = (
    ('XS', 'Extra Small'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Extra  Extra Large'),
    ('XXXL', 'Extra Extra Extra Large'),
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

      
class Category (BaseModel):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name= 'Category'
        verbose_name_plural= 'Categories'
        
    def __str__(self) :
        return self.name


class Color(BaseModel):
    name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name= 'Color'
        verbose_name_plural= 'Colors'
        
    def __str__(self) :
        return self.name    

 
class Product(BaseModel):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.ManyToManyField(Color)
    size = models.CharField(max_length=50, choices=SIZE, default='M')
    like = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    

    class Meta:
        verbose_name= 'Product'
        verbose_name_plural= 'Products'