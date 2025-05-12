import streamlit as st

st.markdown(
    """
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""",
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state.page = "home"


if st.session_state.page == "home":
    st.title("마음 온도계")
    button_write = st.button('감정 일기 쓰기')
    button_stress = st.button('간단한 스트레스 테스트')
    button_graph = st.button('내 데이터 및 통계')

    if button_write:
        st.session_state.page = 'diary'
        st.rerun()
    elif button_stress:
        st.session_state.page = 'stress'
        st.rerun()
    elif button_graph:
        st.session_state.page = 'analysis'
        st.rerun()

elif st.session_state.page == "diary":
    import pages.diary as diary
    diary.show()

elif st.session_state.page == "stress":
    import pages.stress as stress
    stress.show()

elif st.session_state.page == "analysis":
    import pages.analysis as analysis
    analysis.show()
