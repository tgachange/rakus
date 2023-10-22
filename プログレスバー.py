import streamlit as st
import time
# タイトル
st.title('streamlit 超入門2')

# テキスト
st.write('DataFrame')

# プログレスバー
st.write('プログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)


# 2カラムレイアウト
left_column, right_column = st.columns(2)

# 左カラムにボタンを追加
button = left_column.button('ボタンを押すと左カラムに文字表示')
if button:
    # 右カラムにコンテンツを追加
    right_column.write("右カラムに何かコンテンツ")

# エクスパンダー
expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ内容')


