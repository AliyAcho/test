# Подключаем библиотеки
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


def get_sheets(CREDENTIALS_FILE='credentials.json', spreadsheetId='1zXR8GR8E-cnZT-j231ZBcJzp5zLIEeSthsfDuHBFr98'):
    # Читаем ключи из файла
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                      'https://www.googleapis.com/auth/drive'])

    httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
    # Выбираем работу с таблицами и 4 версию API
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    # Берем первый лист
    ranges = ["Лист1!A2:D10000"]
    results = service.spreadsheets().get(spreadsheetId=spreadsheetId,
                                         ranges=ranges, includeGridData=True).execute()

    # Берем строки
    rowData = results['sheets'][0]['data'][0]['rowData']
    first_list = []

    # Пробегаем по строкам и значениям
    for row in rowData:
        if row['values'][0] != {}:
            first_list.append({"№": row['values'][0]['formattedValue'],
                            "заказ №": row['values'][1]['formattedValue'],
                            "стоимость,$": row['values'][2]['formattedValue'],
                            "срок поставки": row['values'][3]['formattedValue']
                            })
    return  tuple(first_list)


# получаем данные из столбца "заказ №"
def get_order_number():
    first_list = []
    rows = get_sheets()
    # Пробегаем по строкам и значениям
    for row in rows:    
        first_list.append(row['заказ №'])
    return  tuple(first_list)