from django.db import models

# Create your models here.
class Trade(models.Model):
    symbol = models.CharField(max_length=30)
    lots = models.DecimalField(max_digits=3, decimal_places=2)
    trade_types_choices = {
        'BUY' : 'BUY', 
        'SELL' : 'SELL'
    }
    trade_type = models.CharField(max_length =4, choices=trade_types_choices)
    take_profit = models.DecimalField(max_digits = 8, decimal_places=5)
    stop_loss = models.DecimalField(max_digits = 8, decimal_places=5)
    close_price = models.DecimalField(max_digits = 8, decimal_places=5)
    open_price = models.DecimalField(max_digits = 8, decimal_places=5)
    entry_time = models.DateTimeField(auto_now = False, auto_now_add=False)
    close_time = models.DateTimeField(auto_now = False, auto_now_add=False)


class Author(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    email = models.EmailField(max_length=60)
    


class Category(models.Model):
    name= models.CharField(max_length=60)


#simple blog post
class Post(models.Model):
    title = models.CharField(max_length=70)
    author= models.ForeignKey(Author,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    content = models.TextField()
    
    


