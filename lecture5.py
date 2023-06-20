# レクチャー5 Wikipediaの情報を取得しよう。

# 5-1 wikipediaをインポートしよう
import wikipedia as wiki

# 5-2 対象とする言語を日本語に設定しよう
wiki.set_lang("ja")

# 5-3 指定したキーワードのページを取得しよう
page = wiki.page("大谷翔平")
print(page)
# 5-4 ページのタイトルと要約を表示しよう
print(page.title)
print(page.summary)

# 5-5 wikipediaに存在しないページを指定してみよう
# page = wiki.page("aaagwegheu")
# print(page.title)
# print(page.summary)

# 5-6 エラーに対する例外処理を記述してみよう。
try:
    page = wiki.page("aaagwegheu")
    print(page.title)
    print(page.summary)
except wiki.exceptions.PageError:
    print("ページが存在しませんでした")