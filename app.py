import streamlit as st
import random
from jamo import h2j, j2hcj

# -------------------------
# 1. 자모 분리 함수
# -------------------------
def to_jamo(word):
    return list(j2hcj(h2j(word)))

# -------------------------
# 2. 단어 리스트 (예시)
#    → 자모 개수가 6개인 단어만 추출
# -------------------------
WORDS = ["책장", "바나나", "고라니", "책상", "인형", "달력"]

# 자모 단위로 변환
JAMO_WORDS = [to_jamo(w) for w in WORDS if len(to_jamo(w)) == 6]

ANSWER = random.choice(JAMO_WORDS)

# -------------------------
# 3. 세션 상태 초기화
# -------------------------
if "guesses" not in st.session_state:
    st.session_state.guesses = []
if "answer" not in st.session_state:
    st.session_state.answer = ANSWER

# -------------------------
# 4. 체크 함수
# -------------------------
def check_guess(guess, answer):
    result = []
    for g, a in zip(guess, answer):
        if g == a:
            result.append("🟩")
        elif g in answer:
            result.append("🟨")
        else:
            result.append("⬜")
    return "".join(result)

# -------------------------
# 5. UI
# -------------------------
st.title("🇰🇷 자모 워들: 꼬들")

st.write("자모 6개 단어 퍼즐 (총 6번 기회)")

guess = st.text_input("자모 6개 입력 (예: ㄱㅏㅂㅏㅇㅣ)", max_chars=6)

if st.button("제출"):
    if len(guess) != 6:
        st.warning("정확히 6개의 자모를 입력하세요!")
    else:
        st.session_state.guesses.append((guess, check_guess(list(guess), st.session_state.answer)))

# -------------------------
# 6. 결과 출력
# -------------------------
for g, r in st.session_state.guesses:
    st.write(f"{g}  {r}")

if st.session_state.guesses and list(st.session_state.guesses[-1][0]) == st.session_state.answer:
    st.success("🎉 정답입니다!")
elif len(st.session_state.guesses) >= 6:
    st.error(f"😭 실패! 정답은 {''.join(st.session_state.answer)}")
