# -*- coding: UTF-8 -*-
import BaseHTTPServer
import json
from ocr import MyModel
import numpy as np
import random
import pandas as pd
#服务器端配置
HOST_NAME = 'localhost'
PORT_NUMBER = 9000
#这个值是通过运行神经网络设计脚本得到的最优值
HIDDEN_NODE_COUNT = 15

# 加载数据集
data = pd.read_csv("/home/chang/my/speech/webcode/data/feature.csv", header=0, delimiter=",")
# 转换成list类型
data_matrix = data.values[:,1:]
data_labels = data.values[:,0]

# 数据集一共5000个数据，train_indice存储用来训练的数据的序号
train_indice = range(252)
# 打乱训练顺序
random.shuffle(train_indice)

nn = MyModel(data_matrix, data_labels);



class JSONHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """处理接收到的POST请求"""
    def do_POST(self):
        response_code = 200
        response = ""
        var_len = int(self.headers.get('Content-Length'))
        content = self.rfile.read(var_len);
        payload = json.loads(content);

        # 如果是训练请求，训练然后保存训练完的神经网络
        if payload.get('train'):
            nn.train(payload['trainArray'])
            nn.save()
        # 如果是预测请求，返回预测值
        elif payload.get('predict'):
            try:
                print nn.predict(data_matrix[0])
                response = {"type":"test", "result":str(nn.predict(payload['image']))}
            except:
                response_code = 500
        else:
            response_code = 400

        self.send_response(response_code)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        if response:
            self.wfile.write(json.dumps(response))
        return

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer;
    httpd = server_class((HOST_NAME, PORT_NUMBER), JSONHandler)

    try:
        #启动服务器
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    else:
        print "Unexpected server exception occurred."
    finally:
        httpd.server_close()

