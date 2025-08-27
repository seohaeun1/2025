import streamlit as st
import random

# -------------------------
# 1. 단어 리스트 준비
# -------------------------
WORDS = ["사과나무", "바나나꽃", "호랑나비", "자동차들", "컴퓨터학"]  # 예시 5글자 단어들
ANSWER = random.choice(WORDS)

# -------------------------
# 2. 세션 상태 초기화
# -------------------------
if "guesses" not in st.session_state:
    st.session_state.guesses = []
if "answer" not in st.session_state:
    st.session_state.answer = ANSWER

# -------------------------
# 3. 함수: 정답 체크
# -------------------------
def check_guess(guess, answer):
    result = []
    for i, ch in enumerate(guess):
        if ch == answer[i]:
            result.append("🟩")  # 위치+글자 맞음
        elif ch in answer:
            result.append("🟨")  # 글자만 맞음
        else:
            result.append("⬜")  # 없음
    return "".join(result)

# -------------------------
# 4. UI
# -------------------------
st.title("🇰🇷 한글 워들: 꼬들")

st.write("5글자 한글 단어를 맞춰보세요! (총 6번의 기회)")

guess = st.text_input("단어 입력", max_chars=5)

if st.button("제출"):
    if len(guess) != 5:
        st.warning("5글자 단어만 입력하세요!")
    else:
        st.session_state.guesses.append((guess, check_guess(guess, st.session_state.answer)))

# -------------------------
# 5. 결과 출력
# -------------------------
for g, r in st.session_state.guesses:
    st.write(f"{g}  {r}")

if st.session_state.guesses and st.session_state.guesses[-1][0] == st.session_state.answer:
    st.success("🎉 정답입니다!")
elif len(st.session_state.guesses) >= 6:
    st.error(f"😭 실패! 정답은 {st.session_state.answer}")
