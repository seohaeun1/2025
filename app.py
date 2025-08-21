import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="작가의 영감 노트 ✨",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS 꾸미기 ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        font-family: "Nanum Myeongjo", serif;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #4B0082;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .quote-box {
        background-color: #fff3e6;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #ff6600;
        font-style: italic;
        font-size: 20px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 명언 데이터 ---
quotes = [
    {"text": "문학은 인간의 내면을 비추는 거울이다. – 톨스토이", "mood": "😢"},
    {"text": "상상력은 지식보다 더 중요하다. – 아인슈타인", "mood": "😊"},
    {"text": "한 줄의 시가 인생을 바꿀 수 있다. – 오든", "mood": "😊"},
    {"text": "소설은 인간에 관한 진실을 드러내는 장치다. – 카프카", "mood": "😢"},
    {"text": "글쓰기는 자기 자신을 발견하는 과정이다. – 조안 디디온", "mood": "😊"},
    {"text": "삶은 짧고 예술은 길다. – 히포크라테스", "mood": "😐"},
    {"text": "시인은 진실을 말하고, 소설가는 그 진실을 증명한다. – 무라카미 하루키", "mood": "😐"},
    {"text": "언어는 존재의 집이다. – 하이데거", "mood": "😐"},
    {"text": "창작은 혼돈에서 질서를 만들어내는 일이다. – 니체", "mood": "😡"},
    {"text": "읽는다는 것은 다른 사람의 생각 속으로 들어가는 일이다. – 움베르토 에코", "mood": "😊"},
    {"text": "위대한 글은 늘 작가 자신을 넘어선다. – 버지니아 울프", "mood": "😐"},
    {"text": "진정한 작가는 말하지 못하는 것을 쓰는 사람이다. – 사르트르", "mood": "😢"},
    {"text": "상처는 글로써 치유된다. – 셰익스피어", "mood": "😢"},
    {"text": "시는 감정이 고요 속에서 회상된 것이다. – 워즈워스", "mood": "😊"},
    {"text": "책은 도끼다. 우리의 얼어붙은 마음의 바다를 깨뜨리는. – 카프카", "mood": "😡"},
    {"text": "작가는 세상을 설명하는 사람이 아니라, 세상에 질문을 던지는 사람이다. – 체호프", "mood": "😐"},
    {"text": "펜은 칼보다 강하다. – 에드워드 불워-리튼", "mood": "😊"},
    {"text": "글을 쓰는 일은 고통이지만, 쓰지 않는 것은 더 큰 고통이다. – 무라카미 하루키", "mood": "😢"},
    {"text": "모든 위대한 작가는 조금씩 미쳤다. – 아리스토텔레스", "mood": "😡"},
    {"text": "단어는 인간의 가장 강력한 무기다. – 키플링", "mood": "😊"}
]

# --- 문학 명대사 데이터 ---
literary_lines = [
    "“지금 슬프냐? 하지만 언젠가는 이 슬픔조차 그리움이 될 것이다.” – 괴테, 젊은 베르테르의 슬픔",
    "“우리는 모두 늪 속에 있지만, 그중 몇몇은 별을 바라본다.” – 오스카 와일드",
    "“내일은 내일의 태양이 떠오를 것이다.” – 마거릿 미첼, 바람과 함께 사라지다",
    "“행복한 가정은 모두 비슷하지만, 불행한 가정은 제각각의 이유로 불행하다.” – 톨스토이, 안나 카레니나",
    "“바람이 분다. 살아야겠다.” – 미야자와 겐지",
    "“지옥은 타인의 시선이다.” – 장 폴 사르트르",
    "“우리는 사랑하기 때문에 존재한다.” – 알베르 카뮈",
    "“죽느냐 사느냐, 그것이 문제로다.” – 셰익스피어, 햄릿",
    "“나는 고백한다, 나는 인간이다.” – 도스토옙스키",
    "“모든 인간은 자유롭게 태어났다.” – 장 자크 루소"
]

# --- 세션 상태 ---
if "saved_quotes" not in st.session_state:
    st.session_state.saved_quotes = []
if "current_quote" not in st.session_state:
    st.session_state.current_quote = None
if "current_line" not in st.session_state:
    st.session_state.current_line = None

# --- 타이틀 ---
st.markdown('<div class="title">✨ 작가의 영감 노트 ✍️</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">오늘의 기분에 맞는 명언, 그리고 문학 속 명대사를 만나보세요.</div>', unsafe_allow_html=True)

# --- 사이드바 (기분 선택) ---
st.sidebar.header("🎭 오늘의 기분")
mood = st.sidebar.radio("기분:", ["😊 행복", "😢 슬픔", "😡 분노", "😐 차분"])

# --- 버튼들 ---
col1, col2 = st.columns(2)
with col1:
    if st.button("오늘의 명언 뽑기"):
        filtered = [q for q in quotes if q["mood"] in mood]
        if filtered:
            st.session_state.current_quote = random.choice(filtered)["text"]
        else:
            st.session_state.current_quote = "해당 기분에 맞는 명언이 아직 준비되지 않았습니다."
with col2:
    if st.button("문학 명대사 뽑기"):
        st.session_state.current_line = random.choice(literary_lines)

# --- 출력 구역 ---
if st.session_state.current_quote:
    st.subheader("📖 오늘의 명언")
    st.markdown(f'<div class="quote-box">{st.session_state.current_quote}</div>', unsafe_allow_html=True)

if st.session_state.current_line:
    st.subheader("🎬 오늘의 문학 명대사")
    st.markdown(f'<div class="quote-box">{st.session_state.current_line}</div>', unsafe_allow_html=True)

# --- 해석 기록 ---
interpretation = st.text_area("✍️ 나의 해석/느낀 점을 적어주세요:", "")

if st.button("💾 저장하기"):
    if interpretation.strip() != "":
        st.session_state.saved_quotes.append(
            {
                "quote": st.session_state.current_quote if st.session_state.current_quote else st.session_state.current_line,
                "my_note": interpretation
            }
        )
        st.success("저장 완료! ✨")
    else:
        st.warning("해석을 입력해주세요!")

# --- 저장된 기록 ---
if st.session_state.saved_quotes:
    st.subheader("📚 나의 영감 저장소")
    for idx, item in enumerate(st.session_state.saved_quotes, 1):
        st.write(f"**{idx}.** {item['quote']}")
        st.write(f"👉 {item['my_note']}")
        st.markdown("---")
