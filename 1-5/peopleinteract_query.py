#interactive queries

import shelve
filednames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in filednames)

db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key: break
    try:
        record = db[key]
    except:
        print('No Such key "%s"!' %key)
    else:
        for field in filednames:
            print(field.ljust(maxfield), '=>', getattr(record, field))