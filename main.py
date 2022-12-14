import django
import sqlite3


print(django.get_version())


class DataBase:
    def __init__(self, db_name: str):
        self.__db_name = f'{db_name}'
        self.__conn = sqlite3.connect(self.__db_name)

    def get_all_item(self, table: str):
        curs = self.__conn.cursor()
        req = f'SELECT name, price, brend, category, description, img_url FROM "{table}"'
        select = curs.execute(req)
        select_data = select.fetchall()
        # print(select_data)
        self.__conn.commit()
        return select_data

    def add_item(self, table: str, data: dict):
        # print(table)
        # print(data)
        columns = ''
        values = ''

        for i in range(len(data.keys())):
            columns += f'"{list(data.keys())[i]}", '
            values += f'"{list(data.values())[i]}", '
        columns = columns[:-2]
        values = values[:-2]

        req = f'INSERT INTO "{table}"' \
                              f' ({columns}) ' \
                              f'VALUES ' \
                              f'({values});'
        # print(req)
        self.__conn.cursor()
        self.__conn.execute(req)
        self.__conn.commit()


db = DataBase('product.sqlite')
text = db.get_all_item('Product_items')
#
# d = {
#     'name': text[0][0],
#     'price': text[0][1],
#     'brend': text[0][2],
#     'category': text[0][3],
#     'description': text[0][4],
#     'images': text[0][5],
# }
cat = []
for i in range(len(text)):
    if text[i][3] not in cat:
        cat.append(text[i][3])

print(cat)
# data = DataBase('db.sqlite3')
# # print(data.)
# for i in range(len(text)):
#     d = {
#         'name': text[i][0],
#         'price': text[i][1],
#         'brend': text[i][2],
#         'category': text[i][3],
#         'description': text[i][4],
#         'images': text[i][5],
#         'availability': 1,
#     }
#     print(d)
#     data.add_item(table='catalog_product', data=d)

list_item = [
    'Фигурки MARVEL',
    'Фигурки DC Comics',
    'Фигурки Disney',
    'Фигурки из Игр',
    'Фигурки Icons',
    'Фигурки из Спорта',
    'Фигурки из Аниме',
    'Фигурки из Музыки',
    'Фигурки из Мультфильмов',
    'Фигурки из Фильмов',
    'Фигурки из Сериалов',
]
