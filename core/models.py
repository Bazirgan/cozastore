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
    image = models.ImageField(upload_to='media/shop/')  

    class Meta:
        verbose_name= 'Product'
        verbose_name_plural= 'Products'
    
    def __str__(self) :
        return self.name     
        

class Blog(BaseModel):
    slug = models.SlugField(max_length = 100, null = True, blank = True, unique = True, )
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/blog/')
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
    
    def __str__(self) :
        return self.title    
    
    def save(self, *args, **kwargs):
        
        
        from core.utils.replace_letter import replace_letter
        
        if not self.slug or self.slug != self.title.lower():
            self.slug = self.title.lower()
            
        return super(Blog, self).save(*args, **kwargs)

class Contact(BaseModel):
    adress = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 50)
    mail = models.EmailField(max_length = 50)
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        
    def __str__(self) :
        return self.adress   
    
class ContactMail(BaseModel):
    email = models.EmailField(max_length = 50)
    message = models.TextField()
    
    class Meta:
        verbose_name = 'ContactMail'
        verbose_name_plural = 'ContactMails'
        
    def __str__(self) :
        return self.email
    
    
class Setting(BaseModel):
   name = models.CharField(max_length=50,null=True,blank=True)
   adress = models.CharField(max_length = 100)
   phone = models.CharField(max_length = 50)
   mail = models.EmailField(null=True,blank=True)
   facebook = models.URLField(null=True,blank=True)
   instagram = models.URLField(null=True,blank=True)
   pinterest = models.URLField(null=True,blank=True)
   logo = models.ImageField(upload_to='media/logo/')
   blog_title = models.CharField(max_length = 100)