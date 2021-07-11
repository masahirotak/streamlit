import streamlit as st
import numpy as np
import pandas as pd
#from PIL import Image
import time

#タイトル
st.title('Streamlit 入門')

#テキストの追加
st.write('Data Frame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#データフレームの表示（表）
st.write(df)

#データフレームの表示　writeと違い、大きさを指定できる
st.dataframe(df.style.highlight_max(axis = 0), width = 300,height = 300)

#テーブルを作成できる　データフレームは動的、静的なのはtable
st.table(df.style.highlight_max(axis = 0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

#乱数データ
df = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)

#折れ線グラフ
st.line_chart(df)

#折れ線グラフ（エリアチャート）
st.area_chart(df)

#棒グラフ
st.bar_chart(df)

#緯度経度データ（東京）
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69 , 139.70],
    columns = ['lat','lon']
)

#地図を表示する
st.map(df)


st.write('Display Image')

"""
#チェックボックスの設置
if st.checkbox('Show Image'):
    #画像読み込み
    img = Image.open('image_6487327.JPG')

    #画像を表示
    st.image(img, caption = 'fuji san', use_column_width = True)
"""

#セレクトボックスの設置
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

#セレクトボックスの値を表示（write不要）
'あなたはの好きな数字は',option,'です。'

#テキスト入力 st.sidebarをつけるとsidebarに表示される
#text = st.sidebar.text_input('あなたの趣味を教えてください')

#テキスト入力 
text = st.text_input('あなたの趣味を教えてください')

#スライダーを表示　最小値、最大値、ディフォルト値
condition = st.slider('あなたの今の調子は？',0,100,50)

'あなたの趣味は',text,'です'
'コンディション：',condition

#カラムを設定
left_column, right_column = st.beta_columns(2)

#ボタンを設置
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

#タブが表示される
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')


st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    #プログレスバーが伸びていっていく
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    #処理が静止する　0だと一瞬で終わる
    time.sleep(0.1)

'Done!!'