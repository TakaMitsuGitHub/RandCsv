import pandas as pd
import random
import string
from datetime import datetime, timedelta


class CreateDf:

    # ランダムな文字列を生成する関数
    @staticmethod
    def __generate_random_string(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    # ランダムな日付文字列を生成する関数
    @staticmethod
    def __generate_random_date():
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 12, 31)
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        formatted_date = random_date.strftime('%Y-%m-%d') # 日付フォーマットを指定

        # Convert the string back to a datetime object
        date_object = datetime.strptime(formatted_date, '%Y-%m-%d')

        return date_object


    def create_df(self):
        # ランダムな文字列と数値を含むDataFrameを作成
        rand_len = 10
        data = {
            'book_id': [f"id_{self.__generate_random_string(10)}" for _ in range(rand_len)],
            'name': [f"book_{self.__generate_random_string(4)}" for _ in range(rand_len)],
            'other': [f"other_{self.__generate_random_string(5)}" for _ in range(rand_len)],
            'rank': [random.randint(1, 100) for _ in range(rand_len)],
            'release_date': [self.__generate_random_date() for _ in range(rand_len)],
        }

        df = pd.DataFrame(data)

        # 欠損値をランダムに挿入する確率を設定（ここでは10%の確率で欠損値を挿入）
        probability = 0.10

        col_name_list = list(df.columns)
        col_name_list.remove('book_id')

        # データフレームに欠損値をランダムに挿入
        for column in col_name_list:
            df[column] = df[column].apply(lambda x: None if random.random() < probability else x)
        print(df)
        return df
