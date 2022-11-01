from abc import ABC, abstractmethod

class Product:
    name = ''
    model = ''
    price = ''
    image = ''
    expiry_date = ''
    weight = ''

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self, product_id):
        pass

    @abstractmethod
    def get_product_by_id(self, product_by_id):
        pass

    @abstractmethod
    def get_all_products (self):
        pass

    @abstractmethod
    def upload_product_image(self, product_id, image):
        pass

    @abstractmethod
    def delete_product (self, product_by_id):
        pass

class ProductManager (ProductAbstract):
    def create_product(self, product: Product):
        print("Product is created")
    def edit_product(self, product_id ):
        print("Editing in progress...  \n Your product has been edited")
    def get_product_by_id(self, product_by_id):
        print("You have chosen a specific product")
    def get_all_products(self):
        print("All products are on display")
    def upload_product_image(self, product_id, image):
        print("Here is the product image")
    def delete_product(self, product_by_id):
        print("product is deleted")

product_manager=ProductManager()

product_manager.upload_product_image(5, 'image')
product_manager.edit_product(2)
product_manager.get_all_products()
        
        
        

        