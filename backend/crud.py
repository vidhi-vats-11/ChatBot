from sqlalchemy.orm import Session
from models import Product, Supplier

def process_query(db: Session, query: str):
    if "brand" in query:
        brand = query.split("brand ")[1]
        products = db.query(Product).filter(Product.brand == brand).all()
        return [product.name for product in products]
    elif "suppliers" in query and "laptops" in query:
        suppliers = db.query(Supplier).filter(Supplier.product_categories.contains("laptops")).all()
        return [supplier.name for supplier in suppliers]
    elif "product" in query:
        product_name = query.split("product ")[1]
        product = db.query(Product).filter(Product.name == product_name).first()
        return f"{product.name}: {product.description} by {product.brand}, priced at {product.price}"
    else:
        return "Query not recognized"