import streamlit as st

write_diary = st.Page("1_diary_write.py", title="일기 쓰기")
stress_test = st.Page("2_stress_test.py", title="스트레스 테스트")
analysis = st.Page("3_analysis.py", title="통계~~~")

page = st.navigation([write_diary, stress_test, analysis])


# 타이틀
st.title('마음 온도계')

# 버튼
button_write = st.button('감정 일기 쓰기')
button_stress = st.button('간단한 스트레스 테스트')
button_graph = st.button('내 데이터 및 통계')

if button_write:
    page = st.navigation([write_diary])
elif button_stress:
    page = st.navigation([stress_test])
elif button_graph:
    page = st.navigation([analysis])



page.run()
