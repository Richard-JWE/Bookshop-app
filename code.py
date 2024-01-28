from main import*


# running the app and defining actions Diti & Ana
def run():
    action = input("Type...\n 1 to update 'inventory'\n 2 to start an order \n 3 to add special requirements or order \n 4 to show customer details \n ")
    if action == '2':      
        start_order()      
    elif action == '1':
        yesType = isEmp()
        if(yesType):
            update_items()    
        else:
            print("You do not have access to update menu")  
    elif action == '4':  
            #  only employee will be able to see customer details
        yesType = isEmp()
        if(yesType):
           show_customer_details()
        else:
            print("You cannot see our customer. You are a user")      
    elif action == '3':
        showing_details(data)
        print("What items do you want to add: ")
        add_order()
    else:
        print(f"Invalid option")
run()



# data for foods, drinks and best selling books - Eanna
data = {
       "books": [
      {
        "name": "Historical",
        "another_name": "War and Peace",
        "writer": "Leo Tolstoy",
        "price": "€24"
      },
      {
        "name": "Romance",
        "another_name": "Gone with the Wind",
        "writer": "Margeret Mitchell",
        "price": "€17.49"
      },
      {
        "name": "Adventure",
        "another_name": "Moby Dick",
        "writer": "Herman Melville",
        "price": "€14.50"
      },
      {
        "name": "Crime",
        "another_name": "The Big Sleep",
        "writer": "Raymond Chandler",
        "price": "€16"
      },
      {
        "name": "Autobiographical",
        "another_name": "The Diary of a Young Girl",
        "writer": "Anne Frank",
        "price": "€12.39"
      }
    ],
    "foods": [
      {
        "name": "Pizza",
        "another_name": "Margherita",
        "price": "€5.99"
      },
      {
        "name": "Burger",
        "another_name": "Cheeseburger",
        "price": "€6.50"
      },
      {
        "name": "Pasta",
        "another_name": "Carbonara",
        "price": "€6"
      },
      {
        "name": "Curry",
        "another_name": "Jalfrezi",
        "price": "€7.50"
      },
      {
        "name": "Vegetarian",
        "another_name": "Falafel",
        "price": "€5.50"
      }
    ],
    "drinks": [
      {
        "name": "Soda",
        "another_name": "Cola",
        "price": "€1.99"
      },
      {
        "name": "Juice",
        "another_name": "Orange Juice",
        "price": "€1.50"
      },
      {
        "name": "Beer",
        "another_name": "Carlsberg",
        "price": "€5.50"
      },
      {
        "name": "Coffee",
        "another_name": "Americano",
        "price": "€3.50"
      },
      {
        "name": "Tea",
        "another_name": "Breakfast",
        "price": "€3"
      }
    ],
   "specials": [
      {
        "name": "Coffee",
        "another_name": "Tropical Brew",
        "price": "€5.99"
      },
      {
        "name": "Fruit Drinks",
        "another_name": "Pineapple Passion Frost",
        "price": "€6.50"
      },
      {
        "name": "Fruit Drinks",
        "another_name": "Watermelon Wave Cooler",
        "price": "€6.70"
      },
      {
        "name": "Tea",
        "another_name": "Island Chai Delight",
        "price": "€5.40"
      },
      {
        "name": "Dessert",
        "another_name": "Mango Tango Cheesecake",
        "price": "€6"
      }
    ]
 
  }
 


# global variable: for using customer information in others functions - Diti
customerOrderDetails = []


# showing menu and books list - Diti
def showing_details(details):
     for item, values in details.items():      
        if item == "books":
            print("Our best-selling books:")
            for book in values:
                print(f"  Name: {book['name']}, Writer: {book['writer']}, Price: {book['price']}")
        elif item == "drinks":
            print(f"Let’s raise a glass to the beginning of Happy Hour and choose your {item}:")
            for drink in values:
                print(f"  Name: {drink['name']}, Price: {drink['price']}")
        else:
            print(f"All of your favorite {item} here:")
            for food in values:
                print(f"  Name: {food['name']}, Another Name: {food['another_name']}, Price: {food['price']}")
   
 
# these are for user          
# taking order from customer: Ana
def get_order():
    choices = input("insert item: ")
    customerOrderDetails.append(choices)
    return choices


# taking customer details: Ana
def get_customer():
    name = input("type your name: ")
    address = input("type your address: ")
    phone = input("type your phone: ")
    customerDetails = {name, address, phone}
    customerOrderDetails.append(customerDetails)
    return customerDetails


# showing completed order to customer: Ana 
def finish_order(items, details="unknown" ):
    print(f"-"*10)
    print(f"{details} Order is completed")
    print(f"Order items: {items}")
    print("Thank you for staying with us")
    # orderDetails = {name, items}
    # return orderDetails
 
#  adding special requirements according to customers - Diti
def add_order():
    addedItems = input("Add items: \n")
    orderDetails = customerOrderDetails.append(addedItems)
    print(f"Order added! You added: {addedItems}")


# starting order from customers and taking data for preferable service - Diti
def start_order():
    print("Do you want to seat here or take away? ")
    service = input("Type your preferable service: here or home\n")


    if(service == 'here'):
        showing_details(data)
        items = get_order()
        print(f"You order - {items}. Thanks!")  
    else:
        showing_details(data)
        items = get_order()
        customerDetails = get_customer()
        # print(customerDetails)
        finish_order(items, customerDetails)


 
# these are for owner


# updating items: owner can update their menu, books - Ana 
def update_items():
     item = input("type the new item: ")
     price = input("type the price: ")
     updatedItems = {item: price}
     print(f"Your updated item is {item} and price is {price}")
     data.update(updatedItems)  
     
# showing customer details - Diti 
def show_customer_details():
    print(customerOrderDetails)


# authenticating user - Richard
def isEmp():
   user_type = input("Are you an employee? (yes/no): ").lower()
   return user_type == 'yes'
 
