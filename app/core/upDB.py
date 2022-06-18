from .sheets import get_order_number, get_sheets
from django.shortcuts import get_object_or_404
from .dollar import get_dollar
import datetime
from .models import Orders
import requests
from app.settings import BOT_TOKEN, CHAT_ID


def update_data():
    rub_course = get_dollar()
    rows = get_sheets()
    check_numbers = get_order_number()
    for row in rows:
        index = int(row["№"])
        order_number = int(row["заказ №"])
        dollar_value = float(row["стоимость,$"])
        ruble_value = round(dollar_value*rub_course, 1)
        delivery_time = datetime.datetime.strptime(
            row["срок поставки"], "%d.%m.%Y").date()
        # Сохраняем новый заказ или проверям значения
        if Orders.objects.filter(order_number=row["заказ №"]).count() == 0:
            order = Orders.objects.create(index=index,
                                          order_number=order_number,
                                          dollar_value=dollar_value,
                                          ruble_value=ruble_value,
                                          delivery_time=delivery_time,
                                          )
            order.save()
        elif Orders.objects.filter(order_number=row["заказ №"]).count() == 1:
            order = get_object_or_404(Orders, order_number=row["заказ №"])
            if order.index != index:
                order.index = index
            if order.dollar_value != dollar_value:
                order.dollar_value = dollar_value
            if order.ruble_value != ruble_value:
                order.ruble_value = ruble_value
            if order.delivery_time != delivery_time:
                order.delivery_time = delivery_time
                if (datetime.date.today() < order.delivery_time) and (order.sending_notification == True):
                    order.sending_notification = False
            order.save()
        # Высылаем уведомление если срок поставки прошел
        if (datetime.date.today() > order.delivery_time) and (order.sending_notification == False):
            send_message(
                message=f"""№ {order.index}\n
                заказ № {order.order_number}\n
                стоимость,$ {order.dollar_value}\n
                стоимость в руб. {order.ruble_value}\n
                прошел срок поставки ({order.delivery_time})
                """
            )
            order.sending_notification = True
            order.save()

    # ??? Если заказ из БД отсутствует в таблице, то мы удаляем его из БД ???
    for order in Orders.objects.all():
        if str(order.order_number) not in check_numbers:
            order.delete()


def send_message(message):
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + \
        '/sendMessage?chat_id=' + CHAT_ID + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)
    return response.json()
