from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class Customer(Model):
    """
    This show a Customer description in database
    """
    CustomerID = fields.UUIDField(pk = True)
    CustomerName = fields.CharField(100)
    CustomerPhoneNumber = fields.CharField(20)
    CustomerAdress = fields.CharField(2000, null = True)
    BuyTime = fields.IntField(null = True)
    Worth = fields.FloatField(null = True)
    created_at = fields.DatetimeField(auto_now_add = True) 
    updated_at = fields.DatetimeField(auto_now = True) 
 
Customer_Pydantic = pydantic_model_creator(Customer, name = 'Customer')
CustomerIn_Pydantic = pydantic_model_creator(Customer, name = 'CustomerIn', exclude_readonly = True)
 

def pydantic_to_tortoise(customer: CustomerIn_Pydantic):
    customer_obj = Customer(
        CustomerCode = customer.CustomerCode,
        CustomerName = customer.CustomerName,
        CustomerPhoneNumber = customer.CustomerPhoneNumber,
        CustomerAdress = customer.CustomerAdress,
    )
    return customer_obj

class Provider(Model):
    """
    This show a Provider description in database
    """
    ProviderID = fields.UUIDField(pk = True)
    ProviderName = fields.CharField(100)
    ProviderAdress = fields.CharField(2000, null = True)
    CategoryList = fields.
    created_at = fields.DatetimeField(auto_now_add = True) 
    updated_at = fields.DatetimeField(auto_now = True) 
 
Provider_Pydantic = pydantic_model_creator(Provider, name = 'Provider')
ProviderIn_Pydantic = pydantic_model_creator(Provider, name = 'ProviderIn', exclude_readonly = True)
 

def pydantic_to_tortoise(provider: ProviderIn_Pydantic):
    provider_obj = Provider(
        ProviderCode = provider.ProviderCode,
        ProviderName = provider.ProviderName,
        ProviderAdress = provider.ProviderAdress,
    )
    return provider_obj