import streamlit as st

st.title("登入範例")

is_logged_in = st.user.get("is_logged_in", False)

if not is_logged_in:
    st.warning("請先登入")
    if "auth" in st.secrets:
        st.button("登入", on_click=st.login)
    else:
        st.info("請先在 .streamlit/secrets.toml 中設定 [auth] 後再使用 st.login。")
    st.stop()

st.success("已登入")
st.write("使用者名稱：", st.user.get("name", ""))
st.write("Email：", st.user.get("email", ""))

st.button("登出", on_click=st.logout)
