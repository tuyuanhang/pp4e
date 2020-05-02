"""
转化行元组的列表为行字典的列表，用字段名作为键名
"""

def makedicts(cursor, query, params=()):
    cursor.execute(query, params)
    colnames = [desc[0] for desc in cursor.description]
    rowdicts = [dict(zip(colnames, row)) for row in cursor.fetchall()]
    return rowdicts

if __name__ == '__main__':
    import sqlite3
    conn = sqlite3.connect('dbase1')
    cursor = conn.cursor()
    cursor.execute('insert into people values(?, ?, ?)', ('Jim','dev',5000))
    query = 'select name, pay from people where pay < ?'
    lowpay = makedicts(cursor, query, [7000])
    for rec in lowpay: print(rec)