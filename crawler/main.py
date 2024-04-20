import json
import requests
import os

company_data = 'company.json'
mapping = 'map.json'
# excel_file = 'all.xlsx'

csv_file = 'all.csv'

# 打开 JSON 文件
with open(company_data, 'r') as file:
    # 读取 JSON 数据
    data = json.load(file)
with open(mapping, 'r') as file:
    # 读取 JSON 数据
    rename_map = json.load(file)
# 设置请求头
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'SF_cookie_4=82505831; _sp_ses.2141=*; SID=e90bcdec-75cb-4892-a64a-88161f4ac082; routeId=.uc1; _sp_id.2141=70c096e1-5fc1-44fb-8884-284e828d8ea8.1713530766.1.1713532143.1713530766.2a6061ac-49d4-4b0e-8663-c64da5f6bbfe; cninfo_user_browse=000007,gssz0000007,*ST%E5%85%A8%E6%96%B0|000010,gssz0000010,%E7%BE%8E%E4%B8%BD%E7%94%9F%E6%80%81|600519,gssh0600519,%E8%B4%B5%E5%B7%9E%E8%8C%85%E5%8F%B0|301529,9900048056,%E7%A6%8F%E8%B5%9B%E7%A7%91%E6%8A%80',
    'Pragma': 'no-cache',
    'Referer': 'http://www.cninfo.com.cn/new/disclosure/stock?stockCode=000007&orgId=gssz0000007',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

i = 0
for index, item in enumerate(data):
    print(
        f"共:{len(data)},当前已爬取:{index + 1},当前进度:{(index + 1) / len(data) * 100}%>>>爬取中>>>{item['zwjc']},代码:{item['code']}")
    # 发送 GET 请求
    detail_data = requests.get(
        'http://www.cninfo.com.cn/data20/financialData/getMainIndicators?scode=' + item['code'] + '&sign=1',
        headers=headers)
    company_info_resp = requests.get(
        'http://www.cninfo.com.cn/data20/companyOverview/getCompanyIntroduction?scode=' + item['code'] + '&sign=1',
        headers=headers)

    if not detail_data.ok:
        print(f">>>爬取失败>>>{item['zwjc']},代码:{item['code']}")
        continue

    company_info = dict()
    if company_info_resp.ok:
        company_info = json.loads(company_info_resp.text)
        basic_information = company_info['data']['records'][0]['basicInformation'][0]
        listing_information = company_info['data']['records'][0]['listingInformation'][0]
        basic_information.update(listing_information)
        company_info = basic_information

    result = json.loads(detail_data.text)
    records = result['data']['records']
    print(f"爬取成功,数据总数:{len(records[0])}")
    # company_name = item['zwjc']

    middle = records[0]['middle']
    for entity in middle:
        entity['类型'] = '中期'

        entity['代码'] = item['code']
    year = records[0]['year']
    for entity in year:
        entity['类型'] = '年报'
        entity['代码'] = item['code']

    one = records[0]['one']
    for entity in one:
        entity['类型'] = '一季报'
        entity['代码'] = item['code']
    three = records[0]['three']
    for entity in three:
        entity['类型'] = '三季报'
        entity['代码'] = item['code']

    _all = middle + year + one + three

    # 保存所有数据的列表
    all_data = []
    for entity in _all:
        new_entity = dict()
        new_entity['所属行业'] = company_info['F032V']
        new_entity['上市日期'] = company_info['F006D']
        new_entity['首发价格'] = company_info['F008N']
        new_entity['公司'] = company_info['ORGNAME']
        for key in entity:
            if entity[key] is None:
                entity[key] = ''
            chinese = rename_map.get(key)
            if chinese:
                new_entity[chinese] = entity[key]
            else:
                new_entity[key] = entity[key]

        all_data.append(new_entity)

    # 获取所有键并按顺序排序
    _columns = sorted(set().union(*[entity.keys() for entity in all_data]))

    if not os.path.exists(csv_file):
        # 创建文件，加表头
        try:
            with open(csv_file, 'a', encoding='GBK') as file_obj:
                _str = ''
                for column in _columns:
                    _str += (column + ',')
                file_obj.write(_str + "\n")

                for entity in all_data:
                    _str = ''
                    for column in _columns:
                        _str += (str(entity[column]) + ',')
                    file_obj.write(_str + "\n")
        except FileNotFoundError as e:
            print("文件未找到", e)
    else:
        # 追加数据
        try:
            with open(csv_file, 'a', encoding='GBK') as file_obj:
                for entity in all_data:
                    _str = ''
                    for column in _columns:
                        _str += (str(entity[column]) + ',')
                    file_obj.write(_str + "\n")
        except FileNotFoundError as e:
            print("文件未找到", e)

print("已全部完成：", csv_file)
