import streamlit as st

# タイトル
st.title("簡易BMI計算機")

# 入力フォーム
height = st.number_input("身長 (cm)", value=170.0)
weight = st.number_input("体重 (kg)", value=60.0)

# 計算ロジック
if st.button("計算する"):
    bmi = weight / ((height / 100) ** 2)
    st.write(f"あなたのBMIは **{bmi:.2f}** です！")
    
    if bmi < 18.5:
        st.warning("低体重です")
    elif bmi < 25:
        st.success("普通体重です")
    else:
        st.error("肥満気味です")