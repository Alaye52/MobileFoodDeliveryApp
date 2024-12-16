import requests

def test_api():
    # 向指定的API端点发送GET请求，此处以查询意大利菜系餐厅为例
    response = requests.get('http://localhost:5000/restaurants?cuisine=Italian')
    # 断言响应的状态码是否为200，200表示请求成功
    assert response.status_code == 200
    # 将响应的内容解析为JSON格式，方便后续对数据进行验证
    data = response.json()
    # 断言返回的数据长度大于0，即确保有数据返回
    assert len(data) > 0
    # 断言返回的所有数据中的'cuisine'字段都等于'Italian'
    assert all(d['cuisine'] == 'Italian' for d in data)

if __name__ == "__main__":
    test_api()