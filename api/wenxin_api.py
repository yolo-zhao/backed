import requests

def query_wenxin_model(query):
    """
    与文心大模型进行API交互，发送用户的查询并获取模型的回答。
    :param query: 用户的查询字符串
    :return: 模型的响应结果
    """
    url = "文心大模型API的URL"  # 替换为文心大模型的实际API URL
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # 如果文心大模型API需要身份认证，替换为实际的API token
        "Content-Type": "application/json"
    }
    data = {
        "query": "我的包裹在哪里"
    }

    try:
        # 发送POST请求到文心大模型的API
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # 检查是否有HTTP错误
        return response.json()  # 返回API响应内容
    except requests.exceptions.RequestException as e:
        # 捕获请求异常并打印错误
        print(f"Error querying Wenxin model: {e}")
        return {"error": "无法连接到文心大模型"}
