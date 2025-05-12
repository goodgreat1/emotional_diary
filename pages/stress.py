import streamlit as st

def show():
    if st.button("← 홈으로"):
        st.session_state.page = "home"
        st.rerun()

    st.title("스트레스 테스트")
    score = 0
    score += st.slider("1. 예상 밖의 일 때문에 속상한 적은 얼마나 있었나요?", 0, 10, 5)
    score += st.slider("2. 인생에서 중요한 일을 제어할 수 없다고 느낀 경우는 얼마나 있었나요?", 0, 10, 5)
    score += st.slider("3. 긴장되고 스트레스를 받았다고 느낀 경우는 얼마나 있었나요?", 0, 10, 5)
    score += st.slider("4. 개인적인 문제를 처리하는 능력에 대해 얼마나 자신감이 없으셨나요?", 0, 10, 5)
    score += st.slider("5. 일들이 당신의 뜻대로 되지 않는다고 느낀 경우는 얼마나 있었나요?", 0, 10, 5)
    score += st.slider("6. 얼마나 자주 화를 억누를 수 없었나요?", 0, 10, 5)
    score += st.slider("7. 해야 할 일을 감당할 수 없다고 느낀적은 얼마나 있었나요?", 0, 10, 5)
    score += st.slider("8. 기분이 매우 좋지 않다고 느낀 적은 얼마나 있었나요?", 0, 10, 5)
    score += st.slider("9. 일들이 잘 안 풀릴 때 얼마나 자주 화를 냈나요?", 0, 10, 5)
    score += st.slider("10. 어려운 일이 과도하게 누적돼 극복할 수 없다고 생각한 경우는 얼마나 있었나요?", 0, 10, 5)

    st.text('*테스트 문제는 연세대학교 세브란스병원 홈페이지에서 가져온 문제입니다*')

    submit = st.button("스트레스 결과 보기")

    if submit:
        st.write("총 점수:", score)
        if score >= 50:
            st.error("스트레스가 높습니다. 휴식이 필요해요.")
        else:
            st.success("스트레스가 낮습니다. 잘 관리하고 있어요.")
