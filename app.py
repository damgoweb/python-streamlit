import requests
import pandas as pd
import streamlit as st

# ホットペッパーAPIのURLとAPIキー
url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
key = ""

# APIに渡すパラメータ
params = {
    "key": key,
    "format": "json",
    "count": 100,
    "large_area": "Z012",
    "genre": "G013",
}

# APIを呼び出してデータを取得
response = requests.get(url, params=params)
data = response.json()

# 取得したデータをPandasのDataFrameに変換
shops = pd.DataFrame([
    {
        "店名": shop["name"],
        "所在地": shop["address"],
        "ジャンル": shop["genre"]["name"],
        "緯度": float(shop["lat"]),
        "経度": float(shop["lng"]),
    }
    for shop in data["results"]["shop"]
])

# Streamlitでデータを表示
st.set_page_config(page_title="Ramen Shops in Kanagawa")
st.title("Ramen Shops in Kanagawa")

st.write(f"Total shops: {len(shops)}")

st.dataframe(shops)



