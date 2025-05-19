import streamlit as st
import pandas as pd
from datetime import datetime
from os import path
 
def show():
    if st.button("← 홈으로"):
        st.session_state.page = "home"
        st.rerun()

    st.title("감정 & 일기 달력")
 
 '''db 존재하는지 확인'''
    if not path.exists("diary.csv"):
        st.info("아직 작성된 일기가 없습니다. 홈에서 일기를 작성해보세요!")
        return

    df = pd.read_csv("diary.csv")
    df["date"] = pd.to_datetime(df["date"])

    selected_date = st.date_input("날짜를 선택하세요", datetime.today())
    selected_entry = df[df["date"].dt.date == selected_date]

    if not selected_entry.empty:
        entry = selected_entry.iloc[0]
        st.markdown("### 📖 선택한 날짜의 일기")
        st.write(f"**날짜:** {selected_date.strftime('%Y-%m-%d')}")
        st.write(f"**기분:** {entry['feels']}")
        st.write(f"**내용:** {entry['context']}")
    else:
        st.warning("이 날짜에는 작성된 일기가 없습니다.")
     
'''일기 쓴 날짜 보여주는거'''
    st.markdown("### 이 날에 일기를 작성하셨어요!")
    diary_dates = sorted(df["date"].dt.date.unique())
    st.write(", ".join(str(d) for d in diary_dates))

'''그래프그려주는거'''
    st.markdown("### 감정 점수 변화 통계")

    emoji_to_score = {
        "😊": 5,
        "🙂": 4,
        "😐": 3,
        "😡": 2,
        "😢": 1
    }
    df["score"] = df["feels"].map(emoji_to_score)
    df = df.sort_values("date")

    chart_df = df.set_index("date")[["score"]]
    st.line_chart(chart_df)

    avg_score = df["score"].mean()
    st.markdown(f"**평균 감정 점수:** {avg_score:.2f}점")

    '''스트레스점수표'''
    df = pd.read_csv("stress.csv")
    stress_df = df.set_index("date")[["stress"]]
    st.line_chart(stress_df)
    avg_score = df["stress"].mean()
    st.markdown(f"**평균 스트레스 점수:** {avg_score:.2f}점")
