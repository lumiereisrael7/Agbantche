from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class Product(Model):
    """
    This shows a Product description in database
    """
    ProductID = fields.UUIDField(pk = True)
    ProductCode = fields.CharField(100, unique = True)
    BarCode = fields.CharField(100, unique = True, null = True)
    ProductName = fields.CharField(100)
    ProductPrice = fields.FloatField()
    ProductDescription = fields.CharField(2000, null = True)
    ProductCategory = fields.CharField(100)
    ReorderQuantitylimit = fields.IntField(default = 20)
    created_at = fields.DatetimeField(auto_now_add = True) 
    updated_at = fields.DatetimeField(auto_now = True) 
    
    def __repr__(self):
        return f'<Product {self.ProductCode} {self.ProductName}>'

class Category(Model):
    """
    This shows a Product description in database
    """
    CategoryID = fields.UUIDField(pk = True)
    CategoryName = fields.CharField(100)
    ProductDescription = fields.CharField(2000, null = True)
    ProductCategory = fields.CharField(100)
    ReorderQuantitylimit = fields.IntField(default = 20)
    created_at = fields.DatetimeField(auto_now_add = True) 
    updated_at = fields.DatetimeField(auto_now = True) 
    
    def __repr__(self):
        return f'<Product {self.ProductCode} {self.ProductName}>'


Product_Pydantic = pydantic_model_creator(Product, name = 'Product')
ProductIn_Pydantic = pydantic_model_creator(Product, name = 'ProductIn', exclude_readonly = True)
 
Action_Pydantic = pydantic_model_creator(Product, name = 'Action')

def pydantic_to_tortoise(product: ProductIn_Pydantic):
    product_obj = Product(
        ProductCode = product.ProductCode,
        BarCode = product.BarCode,
        ProductName = product.ProductName,
        ProductDescription = product.ProductDescription,
        ProductCategory = product.ProductCategory,
        ReorderQuantitylimit = product.ReorderQuantitylimit,
    )
    return product_obj