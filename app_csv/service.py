
import csv
from app_csv.models import Stones, ListNameStone, Client


def read_file(file):
    list_ = list(csv.reader(file.read().decode("UTF-8").splitlines()))
    table = []
    for item in list_[1::]:
        table.append(
            {
                "customer": item[0],
                "item": item[1],
                "total": item[2],
                "quantity": item[3],
                "date": item[4],
            }
        )
    return table


def create_db(data):
    for item in data[1::]:
        if item["item"] not in [listnamestone.name for listnamestone in ListNameStone.objects.all()]:
            listnamestone = ListNameStone.objects.create(name=item["item"])
            listnamestone.save()

        if item["customer"] not in [client.username for client in Client.objects.all()]:
            client = Client.objects.create(username=item["customer"])
            client.save()

        stones = Stones.objects.create(
            customer=Client.objects.get(username=item["customer"]),
            item=ListNameStone.objects.get(name=item["item"]),
            total=item["total"],
            quantity=item["quantity"],
            date=item["date"],
        )
        stones.save()


def clean_db():
    ListNameStone.objects.all().delete()
    Client.objects.all().delete()
    Stones.objects.all().delete()
