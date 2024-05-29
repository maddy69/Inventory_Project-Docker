from ninja import NinjaAPI
from .models import Product
from typing import List
from ninja.orm import create_schema
from django.shortcuts import get_object_or_404

api = NinjaAPI()

ProductSchema = create_schema(Product)

@api.get("/products", response=List[ProductSchema])
def get_all_products(request):
    products = Product.objects.all()
    return products

@api.get("/products/{product_id}", response=ProductSchema)
def get_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return product

@api.put("/products/{product_id}", response=ProductSchema)
def update_product(request, product_id: int, data: ProductSchema):
    product = get_object_or_404(Product, id=product_id)
    for attr, value in data.dict().items():
        setattr(product, attr, value)
    product.save()
    return product

@api.delete("/products/{product_id}")
def delete_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True}
