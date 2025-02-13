from sqlalchemy.orm import Session
from main import engine, Supplier, Product

session = Session(bind=engine)

# Add sample suppliers
supplier1 = Supplier(name="Supplier 1", contact_info="Contact 1", product_categories="Laptops")
supplier2 = Supplier(name="Supplier 2", contact_info="Contact 2", product_categories="Phones")
session.add(supplier1)
session.add(supplier2)

# Add sample products
product1 = Product(name="Laptop A", brand="Brand X", price=1000, category="Laptops", description="A powerful laptop", supplier=supplier1)
product2 = Product(name="Phone B", brand="Brand Y", price=500, category="Phones", description="A smart phone", supplier=supplier2)
session.add(product1)
session.add(product2)

session.commit()
session.close()


