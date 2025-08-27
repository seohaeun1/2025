import streamlit as st
import random

# -------------------------
# 1. 한글 분리 함수 (자모 단위)
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
# 2. 단어 리스트 (자모 6개짜리만)
# -------------------------
WORDS = ["달력", "케이크", "바나나", "책상", "운동", "방랑"]  # 자모 6개 단어 예시
JAMO_WORDS = [split_jamo(w) for w in WORDS if len(split_jamo(w)) == 6]
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
st.title("🇰🇷 자모 워들: 꼬들 (자모 6개 단어만)")

st.write("한글 단어를 입력하면 자동으로 자모 6개로 분리됩니다. (총 6번 기회)")

guess_word = st.text_input("한글 단어 입력 (예: 가방끈, 고양이 등)")

if st.button("제출"):
    guess = split_jamo(guess_word)  # 입력을 자모 단위로 변환
    if len(guess) != 6:
        st.warning("자모로 분리했을 때 정확히 6개가 되는 단어만 입력하세요!")
    else:
        st.session_state.guesses.append(("".join(guess), check_guess(guess, st.session_state.answer)))

for g, r in st.session_state.guesses:
    st.write(f"{g}  {r}")

if st.session_state.guesses and list(st.session_state.guesses[-1][0]) == st.session_state.answer:
    st.success("🎉 정답입니다!")
elif len(st.session_state.guesses) >= 6:
    st.error(f"😭 실패! 정답은 {''.join(st.session_state.answer)}")
