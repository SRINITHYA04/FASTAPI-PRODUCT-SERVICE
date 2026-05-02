from fastapi import FastAPI, HTTPException
from models import Product, Products

app = FastAPI()

@app.get('/')
def greet():
    return "Product Trac Backend"


products=[
    Product(id=1, name="phone",price=99, description="budget phone", quantity=10),
    Product(id=2, name="laptop",price=999, description="gaming laptop", quantity=6),
    Product(id=3, name="pen",price=10, description="A Blue Ink pen", quantity=20),
    Product(id=4, name="power bank",price=199, description="handy current ", quantity=25)
]

# 1. get all the products details
@app.get("/products")
def get_all_prodcuts():
    return products

# 2. get the product detail by Id
@app.get("/products/{prod_id}")
def get_Product(prod_id: int):
    for prod in products:
        if prod.id == prod_id:
            return prod
    raise HTTPException(status_code=404, detail="Data Not Found ")


# 3. Add a new product to the DB
@app.post("/products")
def add_product(Prod_data: Product):
    products.append(Prod_data)
    return Prod_data

# # 4.  Update a product in the DB
@app.patch("/products/{prod_id}")
def update_product(prod_id: int, prod_data: Products):
    for index, prod in enumerate(products):
        if prod.id == prod_id:
            update_data = prod_data.model_dump(exclude_unset=True)

            updated_product = prod.model_copy(update=update_data)

            products[index] = updated_product
            return updated_product

    raise HTTPException(status_code=404, detail="Data Not Found")


#5. Delete a product from DB
@app.delete("/products/{prod_id}")
def delete_a_product(prod_id: int):
    for prod in products:
        if prod.id == prod_id:
            products.remove(prod)
            return prod
    raise HTTPException(status_code=404, detail="Data Not Found ")