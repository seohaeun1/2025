import streamlit as st   # Streamlit 라이브러리 불러오기 (웹앱 제작용)
import random            # 랜덤 모듈 불러오기 (정답 단어를 무작위로 선택하는 데 사용)

# -------------------------
# 1. CSS로 UI 꾸미기 (핑크·보라 테마)
# -------------------------
st.markdown("""   # HTML/CSS를 Streamlit 앱에 삽입
<style>
body {
    background: linear-gradient(to bottom right, #ffe4f0, #e6e6fa);
    /* 전체 배경: 핑크 → 보라 그라데이션 */
}
h1 {
    color: #8A2BE2;   /* 제목 색상 보라 */
    text-align: center;   /* 중앙 정렬 */
}
h3 {
    color: #FF69B4;   /* 소제목 색상 핑크 */
    text-align: center;
}
input[type="text"] {
    background-color: #ffe4f0;   /* 입력창 배경색 */
    border: 2px solid #FF69B4;  /* 테두리 핑크 */
    border-radius: 8px;         /* 둥근 모서리 */
    padding: 6px;               /* 안쪽 여백 */
}
.stButton>button {
    background-color: #FF69B4;  /* 버튼 색상 핑크 */
    color: white;               /* 버튼 글자색 흰색 */
    font-weight: bold;          /* 글자 두껍게 */
    border-radius: 8px;         /* 버튼 둥글게 */
    height: 40px;               /* 버튼 높이 */
    width: 100px;               /* 버튼 너비 */
}
.stButton>button:hover {
    background-color: #FF1493;  /* 버튼에 마우스 올리면 진한 핑크 */
}
</style>
""", unsafe_allow_html=True)   # HTML/CSS를 직접 넣을 수 있도록 허용

# -------------------------
# 2. 한글 분리 함수 (자모 단위)
# -------------------------
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28  
# BASE_CODE: '가'의 유니코드 값
# CHOSUNG: 초성 간격
# JUNGSUNG: 중성 간격

# 초성, 중성, 종성 리스트
CHOSUNG_LIST  = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNGSUNG_LIST = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONGSUNG_LIST = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

def split_jamo(word):
    """단어를 초성/중성/종성 단위로 분리"""
    result = []
    for char in word:   # 입력된 단어의 각 글자 처리
        if '가' <= char <= '힣':   # 한글일 경우
            code = ord(char) - BASE_CODE  # 유니코드 값에서 '가' 뺀 값
            cho  = code // CHOSUNG        # 초성 인덱스
            jung = (code - (CHOSUNG * cho)) // JUNGSUNG  # 중성 인덱스
            jong = (code - (CHOSUNG * cho) - (JUNGSUNG * jung))  # 종성 인덱스
            result.append(CHOSUNG_LIST[cho])   # 초성 추가
            result.append(JUNGSUNG_LIST[jung]) # 중성 추가
            if jong != 0:   # 종성이 있으면
                result.append(JONGSUNG_LIST[jong])
        else:
            result.append(char)   # 한글이 아니면 그대로 추가
    return result

# -------------------------
# 3. 단어 리스트 (자모 6개)
# -------------------------
WORDS = ["달력","케이크","바나나","책상","운동","방랑","날것","코끼리","칠판","모니터","초기화","타자기","공항","심장","긴장","음식","급훈","아파트","현관","어머니","아버지","공간","삼각","러시아","번역","한글","카메라","라디오","안경"]
# 모든 단어 중에서 자모로 분리했을 때 길이가 6인 단어만 선별
JAMO_WORDS = [split_jamo(w) for w in WORDS if len(split_jamo(w)) == 6]

# -------------------------
# 4. 세션 상태 초기화
# -------------------------
if "guesses" not in st.session_state:   # 이전 시도가 없다면
    st.session_state.guesses = []       # 시도 기록 저장용 리스트 생성
if "answer" not in st.session_state:    # 정답 단어가 없다면
    st.session_state.answer = random.choice(JAMO_WORDS)   # 무작위 단어 선택

# -------------------------
# 5. 체크 함수 (블록 색상)
# -------------------------
def check_guess(guess, answer):
    """추측 단어와 정답 단어를 비교해서 색상 반환"""
    result = []
    for g, a in zip(guess, answer):  # 같은 자리끼리 비교
        if g == a:
            result.append("green")   # 글자/위치 모두 일치
        elif g in answer:
            result.append("yellow")  # 글자는 포함되지만 위치 다름
        else:
            result.append("gray")    # 글자 없음
    return result

# -------------------------
# 6. UI
# -------------------------
st.markdown("<h1>🇰🇷 워들: 꼬들</h1>", unsafe_allow_html=True)  # 제목 표시
st.markdown("<h3>자모 6개 단어 맞추기 (총 6번 기회)</h3>", unsafe_allow_html=True)  # 설명 표시

guess_word = st.text_input("한글 단어 입력", max_chars=6)  # 사용자 입력창 (최대 6글자)

# 버튼을 두 개의 열에 배치
col1, col2 = st.columns(2)
with col1:
    if st.button("제출"):
        guess = split_jamo(guess_word)   # 입력 단어 → 자모 분리
        if len(guess) != 6:              # 자모 개수가 6개가 아니면
            st.warning("자모로 분리했을 때 정확히 6개가 되는 단어만 입력하세요!")
        else:
            colors = check_guess(guess, st.session_state.answer)  # 정답과 비교해 색상 결정
            st.session_state.guesses.append(("".join(guess), colors))  # 결과 기록

with col2:
    if st.button("다시하기"):   # 게임 리셋
        st.session_state.guesses = []
        st.session_state.answer = random.choice(JAMO_WORDS)

# -------------------------
# 7. 결과 출력 (블록)
# -------------------------
st.markdown("### 시도 결과")
for g, colors in st.session_state.guesses:   # 모든 시도한 단어 출력
    row_html = ""
    for char, color in zip(g, colors):   # 자모와 색상 매칭
        row_html += f"<span style='display:inline-block;width:32px;height:32px;margin:2px;text-align:center;line-height:32px;background-color:{color};color:white;font-weight:bold;border-radius:4px;'>{char}</span>"
        # HTML span 태그로 색상 박스 생성
    st.markdown(row_html, unsafe_allow_html=True)

# -------------------------
# 8. 정답/실패 체크 + 이펙트
# -------------------------
if st.session_state.guesses:   # 시도가 있을 경우
    last_guess, colors = st.session_state.guesses[-1]   # 마지막 시도 확인
    correct = list(last_guess) == st.session_state.answer  # 정답 여부 확인
    if correct:
        st.success("🎉 정답입니다!")   # 성공 메시지
        st.balloons()                 # 풍선 이펙트
    elif len(st.session_state.guesses) >= 6:   # 6번 실패 시
        st.error(f"😭 실패! 정답은 {''.join(st.session_state.answer)}")
        st.markdown("💥💥💥", unsafe_allow_html=True)  # 실패 이모지 표시
