import streamlit as st
import random

# -------------------------
# 1. CSS로 UI 꾸미기 (핑크·보라 테마)
# -------------------------
st.markdown("""
<style>
/* 전체 배경 */
body {
    background: linear-gradient(to bottom right, #ffe4f0, #e6e6fa);
}

/* 제목 */
h1 {
    color: #8A2BE2;
    text-align: center;
}

/* 소제목 */
h3 {
    color: #FF69B4;
    text-align: center;
}

/* 입력창 */
input[type="text"] {
    background-color: #ffe4f0;
    border: 2px solid #FF69B4;
    border-radius: 8px;
    padding: 6px;
}

/* 버튼 */
.stButton>button {
    background-color: #FF69B4;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    height: 40px;
    width: 100px;
}

/* 버튼 눌렀을 때 */
.stButton>button:hover {
    background-color: #FF1493;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. 한글 분리 함수 (자모 단위)
# -------------------------
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
CHOSUNG_LIST  = [ 'ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ' ]
JUNGSUNG_LIST = [ 'ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ' ]
JONGSUNG_LIST = [ '','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ' ]

def split_jamo(word):
    result = []
    for char in word:
        if '가' <= char <= '힣':
            code = ord(char) - BASE_CODE
            cho  = code // CHOSUNG
            jung = (code - (CHOSUNG * cho)) // JUNGSUNG
            jong = (code - (CHOSUNG * cho) - (JUNGSUNG * jung))
            result.append(CHOSUNG_LIST[cho])
            result.append(JUNGSUNG_LIST[jung])
            if jong != 0:
                result.append(JONGSUNG_LIST[jong])
        else:
            result.append(char)
    return result

# -------------------------
# 3. 단어 리스트 (자모 6개)
# -------------------------
WORDS = ["달력", "케이크", "바나나", "책상", "운동","방랑","날것","코끼리","칠판","모니터","초기화","타자기","공항","심장","긴장","음식","급훈","아파트","현관","어머니","아버지","공간","삼각"]
JAMO_WORDS = [split_jamo(w) for w in WORDS if len(split_jamo(w)) == 6]

# -------------------------
# 4. 세션 상태 초기화
# -------------------------
if "guesses" not in st.session_state:
    st.session_state.guesses = []
if "answer" not in st.session_state:
    st.session_state.answer = random.choice(JAMO_WORDS)

# -------------------------
# 5. 체크 함수 (블록 색상)
# -------------------------
def check_guess(guess, answer):
    result = []
    for g, a in zip(guess, answer):
        if g == a:
            result.append("green")
        elif g in answer:
            result.append("yellow")
        else:
            result.append("gray")
    return result

# -------------------------
# 6. UI
# -------------------------
st.markdown("<h1>🇰🇷 워들: 꼬들</h1>", unsafe_allow_html=True)
st.markdown("<h3>자모 6개 단어 맞추기 (총 6번 기회)</h3>", unsafe_allow_html=True)

guess_word = st.text_input("한글 단어 입력", max_chars=6)

col1, col2 = st.columns(2)
with col1:
    if st.button("제출"):
        guess = split_jamo(guess_word)
        if len(guess) != 6:
            st.warning("자모로 분리했을 때 정확히 6개가 되는 단어만 입력하세요!")
        else:
            colors = check_guess(guess, st.session_state.answer)
            st.session_state.guesses.append(("".join(guess), colors))

with col2:
    if st.button("다시하기"):
        st.session_state.guesses = []
        st.session_state.answer = random.choice(JAMO_WORDS)

# -------------------------
# 7. 결과 출력 (블록)
# -------------------------
st.markdown("### 시도 결과")
for g, colors in st.session_state.guesses:
    row_html = ""
    for char, color in zip(g, colors):
        row_html += f"<span style='display:inline-block;width:32px;height:32px;margin:2px;text-align:center;line-height:32px;background-color:{color};color:white;font-weight:bold;border-radius:4px;'>{char}</span>"
    st.markdown(row_html, unsafe_allow_html=True)

# -------------------------
# 8. 정답/실패 체크 + 이펙트
# -------------------------
if st.session_state.guesses:
    last_guess, colors = st.session_state.guesses[-1]
    correct = list(last_guess) == st.session_state.answer
    if correct:
        st.success("🎉 정답입니다!")
        st.balloons()  # Streamlit에서 동작하는 confetti 대체
    elif len(st.session_state.guesses) >= 6:
        st.error(f"😭 실패! 정답은 {''.join(st.session_state.answer)}")
        st.markdown("💥💥💥", unsafe_allow_html=True)  # 실패 강조
