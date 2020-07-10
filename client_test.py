import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+ quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+ quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_normal(self):
    #test for normal inputs when prices_b!=0
    lsts = [[1,2], [3,4], [0,4], [3,8]]
    for lst in lsts:
      self.assertEqual(getRatio(lst[0], lst[1]), (lst[0]/lst[1]))
  
  def edge_test_getRatio(self):
    #test for edge case when prices_b == 0.
    #expect ZeroDivisionError to be handled gracefully and return 0
    lsts = [[1,0], [2,0], [3,0], [4,0]]
    for lst in lsts:
      self.assertEqual(getRatio(lst[0], lst[1]), 0)




if __name__ == '__main__':
    unittest.main()
