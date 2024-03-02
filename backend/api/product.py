import os, sys

from fastapi import APIRouter, HTTPException, status

from models.Product import Product , pydantic_to_tortoise, ProductIn_Pydantic, Product_Pydantic

folder = os.path.dirname(os.path.abspath('../'))
sys.path.insert(0,folder)

product_router = APIRouter()

# CRUD product
#Add a product in the database
@product_router.post("/products", response_model = Product_Pydantic, name = '/products/create')
async def create_product(product: ProductIn_Pydantic):
    pass
