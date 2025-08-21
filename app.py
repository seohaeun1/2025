import streamlit as st
import random

# --- 명언 데이터 ---
quotes = [
    "문학은 인간의 내면을 비추는 거울이다. – 톨스토이",
    "상상력은 지식보다 더 중요하다. – 아인슈타인",
    "한 줄의 시가 인생을 바꿀 수 있다. – 오든",
    "소설은 인간에 관한 진실을 드러내는 장치다. – 카프카",
    "글쓰기는 자기 자신을 발견하는 과정이다. – 조안 디디온"
]

# --- 세션 상태에 저장 (앱 꺼지기 전까지 기록 유지) ---
if "saved_quotes" not in st.session_state:
    st.session_state.saved_quotes = []

st.title("✨ 작가의 영감 노트 ✍️")
st.write("버튼을 눌러 오늘의 문학 명언을 뽑고, 당신만의 해석을 남겨보세요!")

# 명언 뽑기
if st.button("오늘의 명언 뽑기"):
    st.session_state.current_quote = random.choice(quotes)

# 명언 출력
if "current_quote" in st.session_state:
    st.subheader("📖 오늘의 명언")
    st.info(st.session_state.current_quote)

    # 해석 작성
    interpretation = st.text_area("✍️ 나의 해석/느낀 점:", "")

    if st.button("저장하기"):
        if interpretation.strip() != "":
            st.session_state.saved_quotes.append(
                {"quote": st.session_state.current_quote, "my_note": interpretation}
            )
            st.success("저장 완료! ✨")
        else:
            st.warning("해석을 입력해주세요!")

# 저장된 명언 모아보기
if st.session_state.saved_quotes:
    st.subheader("📚 나의 영감 저장소")
    for idx, item in enumerate(st.session_state.saved_quotes, 1):
        st.write(f"**{idx}.** {item['quote']}")
        st.write(f"👉 {item['my_note']}")
        st.write("---")
