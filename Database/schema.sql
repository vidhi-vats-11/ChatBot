CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_info TEXT,
    product_categories VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(255),
    price FLOAT,
    category VARCHAR(255),
    description TEXT,
    supplier_id INTEGER REFERENCES suppliers(id)
);

INSERT INTO suppliers (name, contact_info, product_categories) VALUES
('Supplier A', 'contact@suppliera.com', 'laptops, phones'),
('Supplier B', 'contact@supplierb.com', 'laptops, tablets');

INSERT INTO products (name, brand, price, category, description, supplier_id) VALUES
('Laptop X', 'Brand X', 999.99, 'laptops', 'High performance laptop', 1),
('Phone Y', 'Brand Y', 499.99, 'phones', 'Latest smartphone', 1),
('Tablet Z', 'Brand Z', 299.99, 'tablets', 'Affordable tablet', 2);