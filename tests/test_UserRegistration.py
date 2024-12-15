# 用户注册功能的单元测试
# Unit tests for user registration functionality
import unittest
from UserRegistration import UserRegistration  # 从UserRegistration模块导入UserRegistration类
 
class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        # 初始化测试环境，创建一个UserRegistration实例
        # Initialize the test environment by creating an instance of UserRegistration
        self.registration = UserRegistration()
 
    def test_valid_registration(self):
        # 测试有效的用户注册
        # Test valid user registration
        result = self.registration.register("user@example.com", "Password123", "Password123")
        # 断言注册成功且返回的消息正确
        # Assert that the registration was successful and the returned message is correct
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], "注册成功，确认邮件已发送")
 
    def test_invalid_email(self):
        # 测试无效的邮箱注册
        # Test registration with an invalid email
        result = self.registration.register("userexample.com", "Password123", "Password123")
        # 断言注册失败且返回的错误信息正确
        # Assert that the registration failed and the returned error message is correct
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "无效的邮箱格式")
 
    def test_duplicate_email(self):
        # 测试重复的邮箱注册（假设有方法模拟这种情况）
        # Test registration with a duplicate email (assuming there's a way to simulate this scenario)
        self.registration.register("user@example.com", "Password123", "Password123")
        result = self.registration.register("user@example.com", "Password456", "Password456")
        # 断言注册失败且返回的错误信息正确
        # Assert that the registration failed and the returned error message is correct
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "邮箱已注册")
 
    # 根据需要添加更多测试
    # Add more tests as needed
 
if __name__ == '__main__':
    unittest.main()  # 运行单元测试