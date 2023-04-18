from django.db import models

# Create your models here.

INDUSTRY_TYPE = (
    ('','Select industry type'),
    ('Computer Industry','Computer Industry'),
    ('Chemical Industries','Chemical Industries'),
    ('Health Services','Health Services'),
    ('Telecommunications Services','Telecommunications Services'),
    ('Textiles: Clothing, Footwear','Textiles: Clothing, Footwear')
)

class CrmCompany(models.Model):
    # logo = models.ImageField(upload_to='images/company',blank=True,null=True)
    name = models.CharField(max_length=150)
    owner_name = models.CharField(max_length=50)
    industry_type = models.CharField(max_length=50,choices=INDUSTRY_TYPE)
    rating = models.CharField(max_length=10)
    location = models.CharField(max_length=150)
    employee = models.CharField(max_length=10)
    website = models.CharField(max_length=150)
    contact_email = models.EmailField(max_length=150,unique=True)
    since = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Crm Companies"
        
    # def get_photo_url(self):
    #     if self.logo and hasattr(self.logo, 'url'):
    #         return self.logo.url
    #     else:
    #         return "/static/images/users/multi-user.jpg"