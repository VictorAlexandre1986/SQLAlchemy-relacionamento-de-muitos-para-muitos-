from config_db import Customer,Product,session

class Crud():

    @staticmethod
    def cadastrar_customer():
        new_user=Customer(
            name="testuser"
        )
    
        new_user2=Customer(
          name="testuser2"
        )

        session.add_all([new_user, new_user2])
        session.commit()


    @staticmethod
    def cadastrar_product():
    
      customer = session.query(Customer).filter_by(id=1).one_or_none()
      customer2 = session.query(Customer).filter_by(id=2).one_or_none()
    
      product=Product(name="Chicken",price=2000)
      product2 = Product(name="Bread",price=1000)
      product3 = Product(name="Milk", price=500)
      
      # customer.products.append(
      #   product,
        
      # )
      customer2.products.append(
        product2
      )
      
      customer2.products.append(
        product3
      )
      session.commit()
      
      print(customer.products)
      
    def deletar():
      customer = session.query(Customer).filter_by(id=1).first()
      product = session.query(Product).filter_by(id=1).first()
      customer.products.remove(product)
      session.commit()
      
      print(customer)
      print(customer.products)
    



