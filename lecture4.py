# レクチャー4 pandasの操作方法

# 4-0 pandasをインポートしよう。
import pandas as pd
students = [('jack', 34, 'Sydeny', 'Australia'),
            ('Riti', 30, 'Delhi', 'India'),
            ('Vikas', 31, 'Mumbai', 'India'),
            ('Neelu', 32, 'Bangalore', 'India'),
            ('John', 16, 'New York', 'US'),
            ('Mike', 17, 'las vegas', 'US')]

# 4-1 リストからデータフレームを作成しよう。列名には名前、年、都市名、国名を設定しよう。
df = pd.DataFrame(students, columns=["Name","Age","City","Country"])
print(df)
# 4-2 Johnさんのデータを表示しよう
print(df[df["Name"] == "John"])
# 4-3 名前にaが含まれるデータを表示しよう
print(df[df.Name.str.contains("a")])

# 4-4 年齢が30才以上の人を探そう
print(df[df.Age >= 30])
print("------")
# 4-5 インド出身で30才以上の人を探そう。（AND条件）
print(df[(df["Age"] >= 30) & (df["Country"] == "India")])
# 4-6 インドもしくはアメリカ出_身の人を探そう。（OR条件）
print(df[(df["Country"] == "US") | (df["Country"] == "India")])