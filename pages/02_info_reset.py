import streamlit as st

st.title("リセット用ページ")

st.subheader("現在保存されている情報")

if 'user_name' in st.session_state and st.session_state.user_name:
    st.write(f"名前：{st.session_state.user_name}")
    st.write(f"学年：{st.session_state.grade}")
    st.write(f"趣味：{'、'.join(st.session_state.hobby)}")
else:
    st.write("なし")

if st.button("入力情報をリセット"):
    st.session_state.user_name=''
    st.session_state.grade=''
    st.session_state.hobby=[]

