import numpy as np
import pandas as pd
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from rest_framework.views import APIView
from rest_framework.response import Response

from .process import rand_df
from . import models


class Index(TemplateView):
    template_name = 'index.html'


# class Store(CreateView):

# API
class CreateCsv(APIView):
    def post(self, request):
        df = rand_df.create_df()
        df.to_csv("items.csv", index=False)
        data = {
            "message": "create成功しました",
        }
        # インスタンス化
        df_to_db = DfToDb(df)
        df_to_db.insertOrUpdate()

        return Response(data)


class ReadCsv(APIView):
    def post(self, request):
        df = pd.read_csv("./items.csv")
        print("read")
        print(df)
        data = {
            "message": "read成功しました",
        }
        # インスタンス化
        df_to_db = DfToDb(df)
        df_to_db.insertOrUpdate()
        return Response(data)


class DfToDb:
    col1 = "name"
    col2 = "other"
    col3 = "rank"
    col4 = "release_date"

    def __init__(self, df):
        self.df = df

    def insertOrUpdate(self):
        for idx, row in self.df.iterrows():
            row = row.replace(np.nan, None)
            models.ReadCsv.objects.update_or_create(
                name=row[self.col1],
                other=row[self.col2],
                release_date=row[self.col4],
                defaults={
                    'rank': row[self.col3],
                }
            )




