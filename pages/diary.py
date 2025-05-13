from os import path
from datetime import datetime
import streamlit as st
import pandas as pd

def show():
    if st.button("← 홈으로"):
        st.session_state.page = "home"
        st.rerun()

    now = datetime.now()
    today = now.date()
    y, m, d = str(today).split("-")
    st.write(f"오늘의 날짜는 {y}년 {m}월 {d}일입니다!")

    feel = st.selectbox(
        "오늘의 기분은 어땠나요?",
        ["😊", "🙂", "😐", "😡", "😢"],
        index=None
    )

    text = st.text_input("일기장", placeholder="일기를 적어보세요!")

    if st.button("일기 저장하기"):
        new_entry = pd.DataFrame([{
        'date': str(today),
        'context': text,
        'feels': feel
    }])

        if path.exists("diary.csv"):
            df = pd.read_csv("diary.csv")
        else:
            df = pd.DataFrame(columns=['date', 'context', 'feels'])

        if str(today) in df['date'].values:
            st.warning("오늘은 이미 일기를 작성하셨어요!")
        else:
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv("diary.csv", index=False)
            st.success("일기가 저장되었습니다!")

