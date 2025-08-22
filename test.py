import streamlit as st
from hanspell import spell_checker

st.set_page_config(page_title="맞춤법 검사기", page_icon="✍️", layout="centered")

st.title("✍️ AI 맞춤법 검사기")
st.write("학교 수행평가용 맞춤법 검사 웹앱입니다!")

# 텍스트 입력
text = st.text_area("검사할 글을 입력하세요:", height=200)

if st.button("맞춤법 검사하기"):
    if text.strip() == "":
        st.warning("텍스트를 입력해주세요!")
    else:
        result = spell_checker.check(text)
        checked_text = result.checked  # 교정된 텍스트
        st.subheader("✅ 교정된 문장")
        st.success(checked_text)

        st.subheader("📊 상세 결과")
        st.json(result.as_dict())
