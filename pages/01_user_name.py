# import streamlit as st

# st.title("ユーザー情報表示ページ")

# if 'user_name' in st.session_state and st.session_state.user_name:
#     st.success(f"こんにちは、{st.session_state.user_name}さん！")
#     st.write(f"学年：{st.session_state.grade}")
#     st.write(f"趣味：{'、'.join(st.session_state.hobby)}")

#     st.snow()

# else:
#     st.error("ユーザー名が設定されていません")
#     st.write("メインページで名前を入力してください")

import streamlit as st

st.title("👤 ユーザー情報表示")

# session_stateからデータを取得して表示
if ('user_name' in st.session_state and st.session_state.user_name):
    st.success("✅ 保存されている情報:")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("名前", st.session_state.user_name)
        st.metric("学年", st.session_state.get('grade', '未設定'))

    with col2:
        if st.session_state.get('hobby'):
            st.write("**趣味:**")
            for hob in st.session_state.hobby:
                st.write(f"• {hob}")
        else:
            st.write("**趣味:** 未設定")

    st.balloons()

else:
    st.error("❌ ユーザー情報が設定されていません")
    st.write("メインページで情報を入力してください")