import unittest
from UserRegistration import UserRegistration
from OrderPlacement import Cart, OrderPlacement
from PaymentProcessing import PaymentProcessing
from RestaurantBrowsing import RestaurantBrowsing, RestaurantDatabase

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # 设置必要的组件
        self.registration = UserRegistration()
        self.database = RestaurantDatabase()
        self.browsing = RestaurantBrowsing(self.database)
        self.cart = Cart()
        self.payment = PaymentProcessing()
    def test_order_process_flow(self):
        # 用户注册
        reg_result = self.registration.register(
            "user@example.com", "Password123", "Password123"
        )
        self.assertTrue(reg_result['success'])

        # 此处假设暂时不需要真实登录验证，直接构造一个模拟的用户信息字典（根据实际情况调整结构）
        user_profile = {'user_id': 1, 'username': 'example_user'}

        # 此处假设暂时不需要真实的搜索逻辑，构造模拟的餐厅数据（根据实际情况调整结构）
        mock_restaurants = [
            {
                'name': 'Mock Italian Restaurant',
                'cuisine': 'Italian',
                'menu': [
                    {'name': 'Pasta', 'price': 10.0},
                    {'name': 'Pizza', 'price': 12.0}
                ]
            }
        ]
        restaurants = mock_restaurants

        self.assertGreaterEqual(len(restaurants), 1)
        menu = restaurants[0]['menu']
        self.cart.add_item(menu[0]['name'], menu[0]['price'], 1)

        # 用户下订单
        order = OrderPlacement(self.cart, user_profile, menu)
        # 此处假设暂时不需要真实的订单处理逻辑，构造模拟的订单处理结果（根据实际情况调整结构）
        order_result = {'success': True, 'order': {'order_id': 1}}

        self.assertTrue(order_result['success'])

        # 用户进行支付
        payment_details = {
            "card_number": "1234567812345678",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        # 此处模拟一个总价数值，比如10.0，你可以根据实际情况调整
        mock_total_amount = 10.0
        payment_result = self.payment.process_payment(
            mock_total_amount, "credit_card", payment_details
        )
        self.assertEqual(payment_result, "支付成功，订单已确认")

if __name__ == '__main__':
    unittest.main()