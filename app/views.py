from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from .process import rand_df

class Index(TemplateView):
    template_name = 'index.html'


# API
# class CreateCsv(APIView):
#     print("APIView")
#
#     def post(self, request):
#         print("post")
#         df = rand_df.create_df()
#         df.to_csv("items2.csv", index=False)
#         data = {
#             "message": "成功しました",
#         }
#         return Response(data)

def create_csv(request):
    data = {
        "message": "成功しました",
        }
    print('create_csv')
    return Response(data)



