import streamlit as st
import time

# タイトル
st.title('Streamlit 超入門2')

# テキスト
st.write('DataFrame')

# プログレスバー
st.write('プログレスバー')
st.text('Start!!')  # スタートのテキストを追加

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')  # イテレーションの進行状況を表示
    bar.progress(i + 1)
    time.sleep(0.1)
