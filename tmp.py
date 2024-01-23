import pandas as pd
import random
import string
from datetime import datetime, timedelta

# ランダムな文字列を生成する関数
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# ランダムな日付文字列を生成する関数
def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')  # 日付フォーマットを指定

# ランダムな文字列と数値を含むDataFrameを作成
rand_len = 10
data = {
    'name': [f"book_{generate_random_string(4)}" for _ in range(rand_len)],
    'other': [f"other_{generate_random_string(5)}" for _ in range(rand_len)],
    'rank': [random.randint(1, 100) for _ in range(rand_len)],
    'release_date': [str(generate_random_date()) for _ in range(rand_len)],
}

df = pd.DataFrame(data)

# 欠損値をランダムに挿入する確率を設定（ここでは10%の確率で欠損値を挿入）
probability = 0.10

# データフレームに欠損値をランダムに挿入
for column in df.columns:
    df[column] = df[column].apply(lambda x: None if random.random() < probability else x)

df.to_csv("items.csv", index=False)
