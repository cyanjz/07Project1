'''
{"대분류":1,"색상":["#EBEBEA","#C6C2C1","#9c9290","#9542c4","#82b747","#d6393f","#5c5c62"],"팔걸이":1,"등받이":1,"다리형태":1}
'''

'''
query output - ~~~
output : list of tuples
order : img_url, name, price, product_url, color_code, material
'''


def build_query_statement(from_extension):
    statement = list()
    for k, v in from_extension.items():
        if k == "대분류":
            # 어느 DB에서 참조해야하는지?
            db_number = int(v)
        else:
            if isinstance(v, list):
                for tag in v:
                    statement.append(k + ' LIKE' + f" '%{tag}%' ")
            else:
                statement.append(k + '=' + f'{v} ')
    statement = "AND ".join(statement)
    DB_dict = {0: 'bed', 1: 'chair'}
    # TODO: table_name 넣어서 query statement 완성할 것. Chair, Bed 구분할 수 있게 db_number(line 17)에 가구 대분류 저장해뒀습니다.
    query_statement = f"SELECT 브랜드, imgurl, name, price, url, 사이즈 FROM {DB_dict[db_number]} WHERE " + statement
    return query_statement


def query_result(output):
    """
    :param output: DB에 query를 날려서 얻은 결과. list of tuples -> [(브랜드, imgurl, name, price, url, size), ...]
    :return: dictionary style for json.
    """
    return {'items' : [{'브랜드': item[0], 'imgurl': item[1], 'name': item[2], 'price': item[3], 'url': item[4], 'size': item[5]} for item in output]}

for test in [
    {
        "대분류": "1",
        "팔걸이": "0",
        "등받이": "1",
        "다리형태": "1"
    },
    {
        "대분류": "1",
        "팔걸이": "0",
        "등받이": "1",
        "다리형태": "1"
    },
    {
        "대분류": "1",
        "팔걸이": "0",
        "등받이": "1",
        "다리형태": "1"
    }
]:
    print(build_query_statement(test))
