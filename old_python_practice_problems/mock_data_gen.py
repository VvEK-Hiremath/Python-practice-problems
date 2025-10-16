import random as rd
import datetime as dtm
from time import sleep

price_dict = {'pid1' : 15,'pid2' : 20,'pid3' : 5,'pid4' : 70,'pid5' : 50,'pid6' : 30}

def gen_data():
    txn_init = 1
    try:
        while True:
            transaction_id =  txn_init
            product_id = rd.choice(['pid1','pid2','pid3','pid4','pid5','pid6']) 
            dtmm = dtm.datetime.now()
            timestamp = dtm.datetime.isoformat(dtmm)
            quantity = rd.randint(1, 10)
            unit_price = price_dict[product_id]
            store_id = rd.choice(['sid1','sid2','sid3'])
            txn_init += 1
            data = [transaction_id,product_id,timestamp,quantity,unit_price,store_id]
            print(data)
            sleep(2)
    except Exception as e:
        print('Stopped data generation : {}'.format(e))

if __name__ == '__main__':
    gen_data()
