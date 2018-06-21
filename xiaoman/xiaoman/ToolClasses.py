import requests
import re

from xiaoman import settings

class Tool(object):
    '''
    getOrder_id 方法从url里提取 order_id ,url为公司详情页url
    order 方法通过（海关数据api）获取订单id，再通过 order_data方法 获取数据
    order_data 方法通过传入的订单id和（点击查看详情后页面api）获取订单数据
    order_data_deal 方法用于每条海关处理数据

    '''
    def getOrder_id(url):
        return re.match('.*company/(.*)\?.*',url).group(1)


    def order(order_id):
        text = requests.get('https://x.xiaoman.cn/'
                            'api/company-read/customs-record?company_type=IMPORT&page=1&page_size=10&id=%s'%order_id
                            , headers=settings.DEFAULT_REQUEST_HEADERS).json()

        content = text['data']['content']
        for i in content:
            Tool.order_data_deal(Tool.order_data( i['id']))


    def order_data(order_data_id):
        url = 'https://x.xiaoman.cn/api/company-read/customs-detail?id=%s' %order_data_id
        data = requests.get(url=url, headers=settings.DEFAULT_REQUEST_HEADERS).json()['data']
        return data
    def order_data_deal(data):
        print(data)

if __name__=='__main__':

    Tool.order(Tool.getOrder_id('https://x.xiaoman.cn/company/2c0cf51b927825c6?name=BALL%20HORTICULTURAL%20COMPANY&referrer=%3AminingResults'))