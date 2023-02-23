from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import preprocessing
import joblib
import streamlit as st


def Milkk():
    st.markdown(
        f"""
    <style>
    .stApp {{
    background-image: url("https://i.pinimg.com/564x/96/5e/a7/965ea70b65abee7193be16817c64d4d2.jpg");
    background-attachment: fixed;
    background-size: cover;
    /* opacity: 0.3; */
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

    st.title('✧ ₊𓍯 โปรแกรมคำนวณคุณภาพของนม ⌒✧🐄')
    st.subheader('𓂂𓉸*゜Awaiting your input°•*⁀➷')  # โชว์errorเมื่อใส่ข้อมูลเข้าไปจะใช้งานได้

    def load_data():
        return pd.read_csv('milknew.csv')

    def save_model(m):
        joblib.dump(m, 'model.joblib')

    def load_model():
        return joblib.load('model.joblib')

    data = load_data()
    label_encoder = preprocessing.LabelEncoder()
    data['Grade'] = label_encoder.fit_transform(data['Grade'])
    data1 = data.drop(['Grade'], axis=1)
    X = data1.drop(['Colour'], axis=1)
    y = data['Grade']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    save_model(model)
    ph = st.slider('ꕁpH (ค่าpH)🧪', 3.0, 9.5)
    st.info('ค่าpHของนมที่ดีควรอยู่ที่ 6.4-6.8')

    temp = st.slider('ꕁTemperature C(อุณหภูมิ)🌡️', 0, 100)
    st.info('อุณหภูมิที่เหมาะสมกับการเก็บนมควรอยู่ที่ ต่ำกว่า15องศา/หรือไม่เกิน40องศา')

    l, r = st.columns(2)
    taste = st.radio('ꕁTaste (รสชาติ)🫙 1 = Good, 0 = Bad', (0, 1))
    st.info('รสชาติของนมที่ดีไม่ควรมีรสชาติเปรี้ยวโดดหรือมีรสขม')

    smell = st.radio('ꕁSmell (กลิ่น)🍓 1 = Good, 0 = Bad', (0, 1))
    st.info(
        'นมที่ดีมักจะไม่ค่อยมีกลิ่นผิดปกติใดๆเลย แต่ทางตรงกันข้ามนมบูดจะมักมีกลิ่นไม่พึงประสงค์ เช่น กลิ่นหืน กลิ่นเหม็นแปลกๆ')

    fat = st.radio('ꕁFat (ไขมัน)🫧 1 = Good, 0 = Bad', (0, 1))
    st.info('ค่าไขมันของนมที่ดีควรไม่น้อยกว่าร้อยละ3.2 หรือให้ดีควรอยู่ที่3.2-3.5')

    turbidity = st.radio('ꕁTurbidity (ความขุ่น)🫧 1 = High, 0 = Low', (0, 1))
    st.info('นมที่ดีควรมีสีขาวหรือเป็นสีของกลิ่นรสชาตินมนั้นๆ ไม่ควรมีลักษะตกตะกอนเป็นสีใสหรือเป็นก้อน')

    preb = st.button('Prediction')
    if preb:
        model = load_model()
        predic = model.predict([[ph, temp, taste, smell, fat, turbidity]])
        if predic[0] == 0:
            st.write('Quality of milk is :red[low]')
        elif predic[0] == 1:
            st.write('Quality of milk is :orange[medium]')
        else:
            st.write('Quality of milk is :green[high]')



    st.subheader('ᗯᗩITIᑎG ᖴOᖇ YOᑌ TO ᑕᒪIᑕK TO ᖇᕮᗩᗪ ˚ ༘♡ 𝐫𝐢𝐠𝐡𝐭 𝐛𝐚𝐫 👈')
