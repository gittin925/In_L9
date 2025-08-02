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

# import streamlit as st

# st.title("🔄 データリセット")

# st.write("保存されているユーザー情報をリセットします")

# # 現在の情報を表示
# if st.session_state.get('user_name'):
#     st.info("現在保存されている情報:")
#     st.write(f"名前: {st.session_state.get('user_name', '未設定')}")
#     st.write(f"学年: {st.session_state.get('grade', '未設定')}")
#     st.write(f"趣味: {', '.join(st.session_state.get('hobbies', []))}")

#     if st.button("🗑️ すべての情報をリセット", type="primary"):
#         st.session_state.user_name = ""
#         st.session_state.grade = ""
#         st.session_state.hobbies = []
#         st.success("✅ すべての情報をリセットしました！")
#         st.rerun()  # ページを再読み込み
# else:
#     st.warning("リセットする情報がありません")