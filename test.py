import streamlit as st
from pnu_open_hanspell import spell_checker

st.set_page_config(page_title="맞춤법 검사기", page_icon="✍️")

st.title("✍️ 맞춤법 검사기 (안정 버전)")
text = st.text_area("검사할 문장을 입력하세요:")

if st.button("검사하기"):
    if text.strip():
        result = spell_checker.check(text)
        st.subheader("✅ 교정된 문장")
        st.success(result.checked)

        st.subheader("📊 상세 결과")
        st.json(result.as_dict())
    else:
        st.warning("문장을 입력해주세요!")
