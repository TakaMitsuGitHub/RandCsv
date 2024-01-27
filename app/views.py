import numpy as np
import pandas as pd
import pandera as pa
from pandera import DataFrameSchema, Column, Check
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from rest_framework.views import APIView
from rest_framework.response import Response

from pydantic import BaseModel, ValidationError, constr
from django.db import models

from .process import rand_df
from . import models


class Index(TemplateView):
    template_name = 'index.html'


# API
class CreateCsv(APIView):
    def post(self, request):
        create_df = rand_df.CreateDf()
        df = create_df.create_df()
        df.to_csv("items.csv", index=False)
        data = {
            "message": "create成功しました",
        }
        return Response(data)


class ReadCsv(APIView):
    def post(self, request):
        df = pd.read_csv("./items.csv")
        # 欠損値を0に置き換える
        df['rank'] = df['rank'].fillna(0)
        # 整数型に変換
        df['rank'] = df['rank'].astype(int)
        # DateTime型に変換
        df['release_date'] = pd.to_datetime(df['release_date'],
                                            errors='coerce')
        mapping_dic = {
            "col0" : "book_id",
            "col1" : "name",
            "col2" : "other",
            "col3" : "rank",
            "col4" : "release_date",
        }

        df_schema = DataFrameSchema({
            "book_id": Column(pa.String),
            "name": Column(pa.String, nullable=True),
            "other": Column(pa.String, nullable=True),
            "rank": Column(pa.Int32, checks=Check.greater_than_or_equal_to(0)),
            "release_date": Column(pa.DateTime, nullable=True)
        })

        validator = DataFrameValidator(df_schema)
        validated_df, validated_mapping = validator.validate(df, mapping_dic)

        df_to_db = DfToDb(validated_df, validated_mapping)
        df_to_db.insertOrUpdate()

        data = {
            "message": "read&insert成功しました",
        }
        return Response(data)


# バリデーション用クラス
class DataFrameValidator:
    class MappingModel(BaseModel):
        col0: constr(strict=True)
        col1: constr(strict=True)
        col2: constr(strict=True)
        col3: constr(strict=True)
        col4: constr(strict=True)

    def __init__(self, df_schema):
        self.df_schema = df_schema

    def validate(self, df, mapping_dic):
        # Panderaを使用してDataFrameのバリデーション
        try:
            validated_df = self.df_schema(df)
        except pa.errors.SchemaError as e:
            raise ValueError(f"DataFrame validation failed: {e}")

        # Pydanticを使用してmappingのバリデーション
        try:
            validated_mapping = self.MappingModel(**mapping_dic)
        except ValidationError as e:
            raise ValueError(f"Mapping validation failed: {e}")

        return validated_df, validated_mapping.model_dump()


class DfToDb:
    def __init__(self, df, mapping):
        self.__df = df
        self.__mapping = mapping

    def insertOrUpdate(self):
        for idx, row in self.__df.iterrows():
            row = row.replace(np.nan, None)
            models.BookId.objects.update_or_create(
                book_id=row[self.__mapping["col0"]],
                defaults={}
            )
            models.ReadCsv.objects.update_or_create(
                book_id=row[self.__mapping["col0"]],
                name=row[self.__mapping["col1"]],
                other=row[self.__mapping["col2"]],
                release_date=row[self.__mapping["col4"]],
                defaults={
                    'rank': row[self.__mapping["col3"]],
                }
            )
