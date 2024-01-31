import pandas as pd
import os

from dataclasses import dataclass

from pro import settings


# @dataclass
# class Dclass:
#     point: int


@dataclass(frozen=True)
class Calclass():
    point: int
    point2: float
    point3: str = "aaa"

    def csv_read(self):
        file_path = os.path.join(settings.BASE_DIR, "items.csv")
        df = pd.read_csv(file_path)
        print(self.point)
        print(self.point2)
        print(self.point3)
        print('qqqq')
        print(df)

