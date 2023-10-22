import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# タイトル
st.title('streamlit 超入門')

# テキスト
st.write('DataFreame')

# 表の作成
df =pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
# 表の大きさの表示
st.dataframe(df)
# 表の大きさ変更
st.dataframe(df,width=1000,height=200)
# ハイライトの設定
st.dataframe(df.style.highlight_max(axis=0))

# マークダウン
"""
# 章
## 節
### 項


'''python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""

# チャート
# ランダムな数値の生成
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.dataframe(df2)
# グラフの作成
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

# チャート
# 地図の表示
df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.dataframe(df3)
# 地図の作成
st.map(df3)

# 写真の表示
# st.write('Display Image')

# チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('HOME-PC - 1920-1200.jpg')
    st.image(img, caption='car',use_column_width=True)

# セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を入れてください',
    list(range(1,11))
)
'あなたが好きな数字は',option,'です'

# # インタラクティブなウィジェット
# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は',text,'です'

# # スライダー
# condition = st.slider('あなたの体調は？',0,100,50)
# 'コンディション：',condition

# # サイドバー
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの体調は？',0,100,50)

# 2カラムレイアウト
# left_colum,right_colum = st.beta_columns(2)
# left_colum.button('右からむに文字表示')



text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの体調は？',0,100,50)

'あなたの趣味は：',text
'コンディション：',condition