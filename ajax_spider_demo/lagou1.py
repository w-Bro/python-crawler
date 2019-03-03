import requests
from lxml import etree


def request_list_page():
    cookies = {
        '_ga': 'GA1.2.1083537074.1547639998',
        'user_trace_token': '20190116195957-3e85e579-1986-11e9-b67a-5254005c3644',
        'LGUID': '20190116195957-3e85ea48-1986-11e9-b67a-5254005c3644',
        'index_location_city': '%E5%B9%BF%E5%B7%9E',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22168b1fdda26183-03504571f687d-b781636-2073600-168b1fdda277ab%22%2C%22%24device_id%22%3A%22168b1fdda26183-03504571f687d-b781636-2073600-168b1fdda277ab%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
        'JSESSIONID': 'ABAAABAAAFCAAEG5D568925B40D08FCE35C7188A5020C16',
        '_gid': 'GA1.2.402896183.1550197066',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548305915,1549169437,1549195341,1550197066',
        'LGSID': '20190215101744-e168f4d2-30c7-11e9-81ea-5254005c3644',
        'PRE_UTM': '',
        'PRE_HOST': '',
        'PRE_SITE': '',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
        'TG-TRACK-CODE': 'search_code',
        '_gat': '1',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1550197185',
        'LGRID': '20190215101943-283cdf78-30c8-11e9-81ea-5254005c3644',
        'SEARCH_ID': '01120f69712d4a74afbd6db0a198290c',
    }

    headers = {
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cache-Control': 'no-cache',
        'Referer': 'https://www.lagou.com/jobs/list_python?&px=default&city=%E5%B9%BF%E5%B7%9E',
        'X-Anit-Forge-Token': 'None',
    }

    params = (
        ('px', 'default'),
        ('city', '\u5E7F\u5DDE'),
        ('needAddtionalResult', 'false'),
    )

    data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python'
    }

    response = requests.post('https://www.lagou.com/jobs/positionAjax.json', headers=headers, params=params,
                             cookies=cookies, data=data)
    # json(): 如果返回的是json数据，这个方法会自动load成字典
    print(response.json())


def main():
    request_list_page()


if __name__ == '__main__':
    main()