import streamlit  as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Progress bar')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)




left_column, right_column = st.columns(2)
button = left_column.button('Display on the right column')
if button:
    right_column.write('This is the right side')

expander = st.expander('Query')
expander.write('Write something on query')
expander.write('Write something on query')
expander.write('Write something on query')
expander.write('Write something on query')




# text = st.text_input('Tell me your hobby')
# condition = st.slider('How well are you doing?', 0, 100, 50)

# 'Your hobby: ', text
# 'condition: ',condition 

# option = st.selectbox(
#     'Choose your favorite number',
#     list(range(1, 11))
# )
# 'Your favorite number is ', option, ',right?'

# if st.checkbox('Show Image'):
#     img = Image.open('disney-wallpaper-hd-best-disney-wallpaper-widescreen-cartoons-page-on-all-hd-listed-images-for.jpg')
#     st.image(img, caption='UP', use_column_width=True)


# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)


