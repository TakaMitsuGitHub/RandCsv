from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from .process import rand_df

class Index(TemplateView):
    template_name = 'index.html'


# API
class CreateCsv(APIView):
    def post(self, request):
        print("post")
        df = rand_df.create_df()
        print(df)
        df.to_csv("items.csv", index=False)
        data = {
            "message": "成功しました",
        }
        print("data")
        print(data)
        return Response(data)




