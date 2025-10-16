import random
import time

data_list = []

def generate_data():
    """Generate random order data."""
    orderid = str(random.randint(1, 10000))  # Random order ID between 1 and 10000
    product_name = random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'])
    quantity = random.randint(1, 5)
    price = float(str(round(random.uniform(10.0, 500.0), 2)))
    
    return {
        'orderid': orderid,
        'product_name': product_name,
        'quantity': quantity,
        'price': price
    }

a=10

try:
    while a>0:
        cd = generate_data()
        data_list.append(cd)
        a-=1
except KeyboardInterrupt:
    print("keyboard interruption detected!!")

'''
if __name__ == '__main__':
    try:
        while True:
            print(generate_data())
            time.sleep(2)
    except KeyboardInterrupt:
        print("keyboard interruption detected!!")
else:
    print("file was imported cannot generate data...")
'''
