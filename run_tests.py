import unittest

if __name__ == '__main__':
    # 创建测试加载器，用于发现指定目录下的所有测试用例
    loader = unittest.TestLoader()
    # 从'tests'目录及其子目录下发现所有以'test_'开头的测试文件中的测试用例
    tests = loader.discover('tests', pattern='test_*.py')
    # 创建文本测试运行器，用于执行测试并输出结果到控制台
    test_runner = unittest.TextTestRunner()
    # 运行发现的所有测试用例
    test_runner.run(tests)