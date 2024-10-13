from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image 
#define the ORM Class
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories')
    domain_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='categories')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='added_categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    DRAFT= 'Draft'
    WAITING_APPROVAL= 'Waiting Apruval'
    ACTIVE = 'active'
    DELETE = 'delete'
    STATUS_CHOICES = (
        (DRAFT,'Draft'),
        (WAITING_APPROVAL,'Waiting Apruval'),
        (ACTIVE,'active'),
        (DELETE, 'delete')
    )
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="product_images", null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True, null=True)
    specifications = models.JSONField(blank=True, null=True)
    initial_sell = models.FloatField(blank=True, null=True)
    initial_buy = models.FloatField(blank=True, null=True)
    dimensions = models.CharField(default='0x0x0', max_length=255)
    color = models.CharField(max_length=255)
    tax_percentage = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255)
    brand_model = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=ACTIVE)
    additional_details = models.JSONField(blank=True, null=True)
    display_order = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='variants')
    domain_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Default to user with ID=1
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class ProductQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    status = models.CharField(max_length=30, blank=True, null=True, choices=(('Active', 'Active'), ('Disabled', 'Disabled')))
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True, related_name='questions')
    domain_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='questions_domain_user')
    question_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='questions_asked_by')
    answer_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='questions_answered_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductReview(models.Model):
    id = models.AutoField(primary_key=True)
    review_images = models.ImageField(blank=True, null=True)  # Use blank=True, null=True for optional fields
    rating = models.FloatField()
    review = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    domain_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='product_reviews')
    review_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='reviews_written_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review for {self.product.name} by {self.review_user.username}'
class Order (models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    STATUS_CHOICES = (
        (ORDERED,'ordered'),
        (SHIPPED,'shipped')
       )
     
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    posta_code = models.CharField(max_length=20, default='0000')
    marchent_id = models.CharField(max_length=255)
    paid_amount =models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES,default='ORDERED')
   
    class Meta:
        ordering = ('-created_at',)
    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.price
