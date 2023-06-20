# レクチャー6 ファイルの操作方法について学ぼう

# 6-1 テストの点数が記載されたテキストファイル(Number.txt)を作成しよう。
# A,90,88,60
# B,78,67,90

# 6-2 ファイルを読み込んで表示しよう。
with open("number.txt") as open_file:
    text_data = open_file.read()
print(text_data)

# 6-3 "I Love Coding!!"と書かれたファイル(written.txt)を作成しよう。
with open("written.txt", "w") as write_file:
    write_file.write("I Love Coding!!")

# 6-4 作成したファイルを表示しよう。

# 6-5 "MacBookPro"とファイルを上書きしてみよう。
with open("written.txt", "w") as update_file:
    update_file.write("MacBookPro")

# 6-6 改行コードを挟んで2行の文字列を書き出してみよう。（改行コードはoption + ¥）
with open("written.txt", "w") as update_file:
    update_file.write("MacBookPro 1\n")
    update_file.write("MacBookPro 2")