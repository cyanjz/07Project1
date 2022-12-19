
def build_query_statement(from_extension, cur, columns):
    """
    :param from_extension: class which items() method return iterator of tuple of key and value.
    :param cur: DB cursor object.
    :param columns: Object to handle different column names in different DBs.
    :return: DB fetched result. {items : [{col1 : val1, col2 : val2, ...}, ...]}
    """
    statement = list()
    DB_dict = {'0': 'bed', '1': 'chair'}
    for k, v in from_extension.items():
        if v is None:
            pass
        else:

            if k == "대분류":
                db_number = str(v)                
            else:
                if isinstance(v, list):
                    for tag in v:
                        statement.append(k + ' LIKE' + f" '%{tag}%' ")
                else:
                    if k == '브랜드':
                        statement.append(k + '=' + "'" + f'{v}' + "' ")
                    else:
                        statement.append(k + '=' + f'{v} ')
    statement = "AND ".join(statement)

    query_statement = f"SELECT 브랜드, imgurl, name, price, url, 사이즈, 주요재질, 색상태그, {','.join(columns[db_number][1:])} FROM {DB_dict[db_number]} WHERE " + statement
    result = cur.execute(query_statement).fetchall()
    filtered_result = list()
    while len(result) != 0:
        row = result.pop()
        same_rows = [i for i in result if i[2] == row[2]]
        result = [i for i in result if i[2] != row[2]]
        if len(same_rows) != 0:
            for same_row in same_rows:
                row = [row[i] if str(same_row[i]) in str(row[i]) else str(row[i]) + '/' + str(same_row[i]) for i in range(len(row))]
        filtered_result.append(row)

    target_col = ['브랜드', 'imgurl', 'name', 'price', 'url', '사이즈', '주요재질', '색상태그']
    response = {'items' : list()}   
    target_col.extend(columns[db_number][1:])

    for item in filtered_result:
        dummy = {k: v for k, v in zip(target_col, item)}
        dummy['가구'] = db_number
        response['items'].append(dummy)
    
    return response




def query_result(output):
    """
    Not used.
    """
    return {'items' : [{'브랜드': item[0], 'imgurl': item[1], 'name': item[2], 'price': item[3], 'url': item[4], 'size': item[5]} for item in output]}
