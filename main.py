import streamlit as st

# MBTI별 직업 추천 데이터
career_dict = {
    "INTJ": ["전략가", "과학자", "기획자"],
    "ENTP": ["창업가", "마케터", "프로듀서"],
    "INFJ": ["상담가", "작가", "심리학자"],
    "ESFP": ["연예인", "이벤트 플래너", "광고 전문가"],
    # ... 나머지 MBTI도 추가 가능
}

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟")

st.title("🌟 MBTI 기반 진로 추천 웹앱")
st.write("당신의 MBTI를 선택하면 어울리는 직업을 추천해드립니다!")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요", list(career_dict.keys()))

# 추천 버튼
if st.button("직업 추천 받기"):
    st.subheader(f"🔎 {mbti} 유형에게 어울리는 직업")
    for job in career_dict[mbti]:
        st.write(f"- {job}")

