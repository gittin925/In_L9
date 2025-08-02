import streamlit as st

st.title("ユーザー情報入力")

# if 'user_name' not in st.session_state:
#     st.session_state.user_name=''

# user_name = st.text_input("あなたの名前を入力してください")

# if st.button("名前を保存"):
#     st.session_state.user_name=user_name
#     st.success("名前を保存しました!")

# st.write(f"現在保存されている名前：{st.session_state.user_name}")

if 'user_name' not in st.session_state:
    st.session_state.user_name=''
if 'grade' not in st.session_state:
    st.session_state.grade=''
if 'hobby' not in st.session_state:
    st.session_state.hobby=''

user_name=st.text_input("名前を入力")
grade=st.selectbox("学年",["小学5年","小学6年","中学1年","中学2年","中学3年","大学4年"])
hobby=st.multiselect("趣味",["読書","スポーツ","ゲーム","音楽","絵画","その他"])
if "その他" in hobby:
    others=st.text_input("その他の趣味を入力(空白で区切る)")
    if others:
        hobby.remove("その他")
        hobby+=others.split()

try:
    if st.button("情報を保存"):
        st.session_state.user_name=user_name
        st.session_state.grade=grade
        st.session_state.hobby=hobby
        st.success("情報を保存しました")
except:
    st.write("入力が不足しています")