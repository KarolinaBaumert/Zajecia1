import os


dirs = [
    "ecommerce",
    "ecommerce/product",
    "ecommerce/order"
]

files = {
    "ecommerce/__init__.py": "",
    "ecommerce/main.py": "",
    "ecommerce/utils.py": "",
    "ecommerce/product/__init__.py": "",
    "ecommerce/product/product.py": "",
    "ecommerce/order/__init__.py": "",
    "ecommerce/order/order.py": "",
}


for dir_path in dirs:
    os.makedirs(dir_path, exist_ok=True)


for file_path, content in files.items():
    with open(file_path, 'w') as f:
        f.write(content)

print("Structure created successfully!")
