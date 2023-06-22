import streamlit as st
import numpy as np
import pandas as pd

# タイトル表示
st.title('Streamlit 使い方')

# テキスト追加
st.write('DataFrame')

df = pd.DataFrame({
'1列目':[1,2,3,4],
'2列目':[10,20,30,40]
})
st.write(df)

# dataframeでテーブル表示 + ハイライト
st.dataframe(df.style.highlight_max(axis=0), width=200,height=400)
# tableで表示 + ハイライト
st.table(df.style.highlight_max(axis=0))