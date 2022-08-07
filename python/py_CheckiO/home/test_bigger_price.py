import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def bigger_price(limit, data):
	prices = [i["price"] for i in data]	
	most_expensive = []
	for x in range(limit):
		c = max(prices)
		for item in data:
			if item["price"] == c:
				most_expensive.append(item)
				prices.pop(prices.index(max(prices)))
	return most_expensive						

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#import operator, heapq, functools
#bigger_price = functools.partial(heapq.nlargest, key=operator.itemgetter('price'))

#def bigger_price(limit, data):
	#return sorted(data, key=lambda x: x['price'], reverse = True)[:limit]

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestBiggerPrice(unittest.TestCase):
    def test_two_biggest_prices(self):
        self.assertEqual(bigger_price(
            2, 
            [{"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1}]
            ),
            [{"name": "wine", "price": 138}, 
            {"name": "bread", "price": 100}]
        )	
    
    def test_biggest_price(self):
        self.assertEqual(bigger_price(
            1, 
            [{"name": "pen", "price": 5},
            {"name": "whiteboard", "price": 170}]
            ),
            [{"name": "whiteboard", "price": 170}]
        ) 


if __name__ == '__main__':
	unittest.main()
