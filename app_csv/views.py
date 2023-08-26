
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from app_csv.models import Stones, Client
from app_csv.serializers import ClientSerializer
from app_csv.service import clean_db, create_db, read_file


class StonesView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        for obj in Stones.objects.all():
            if obj.item not in obj.customer.gems.all():
                obj.customer.gems.add(obj.item)
            obj.customer.spent_money += obj.total
            obj.customer.save()

        queryset = Client.objects.order_by('-spent_money')[:5]
        gems_list = []

        for client in queryset:
            gems_list += client.gems.all()
        for client in queryset:
            i = 0
            gems = client.gems.all()
            while i < len(gems):
                if gems_list.count(gems[i]) == 1:
                    client.gems.remove(gems[i])
                    client.save()
                i += 1

        serializer = ClientSerializer(data=queryset, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)

    def post(self, request):
        content_type = request.content_type.split(';')[0].strip()

        if content_type == "multipart/form-data":
            file = request.data.get("deals")
            try:
                file.name.split('.')[1] != "csv"
            except AttributeError:
                return Response("Формат файла не .csv", status.HTTP_400_BAD_REQUEST)
            table = read_file(file)
            clean_db()
            create_db(table)
            return Response("Файл успешно загружен", status.HTTP_201_CREATED)
