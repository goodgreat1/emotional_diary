import streamlit as st

def show():
    if st.button("← 홈으로"):
        st.session_state.page = "home"
        st.experimental_rerun()

    st.title("스트레스 테스트")
