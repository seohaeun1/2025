import streamlit as st
import random

# -----------------------
# 페이지 설정
# -----------------------
st.set_page_config(
    page_title="작가의 영감 노트 ✨",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------
# 데이터: 오늘의 명언 (20개)
# -----------------------
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

# -----------------------
# 데이터: 문학 명대사 (30개)
# -----------------------
literary_quotes = [
    "“나는 나의 폐허를 사랑한다.” – 보들레르",
    "“모든 것은 지나가리라.” – 톨스토이",
    "“오늘 내가 사는 것은 어제 죽은 이들이 그토록 살고 싶었던 내일이다.” – 투르게네프",
    "“네가 가진 것 중 오직 너 자신만이 진짜 너다.” – 카프카",
    "“우리는 모두 같은 하늘을 바라보지만, 서로 다른 지평선을 본다.” – 츠바이크",
    "“달은 차가워도 빛을 잃지 않는다.” – 동양 격언",
    "“나는 고통 속에서도 시를 쓴다. 그것이 나의 해방이니까.” – 릴케",
    "“나는 운명이 아니면 아무것도 믿지 않는다.” – 도스토예프스키",
    "“죽느냐 사느냐, 그것이 문제로다.” – 셰익스피어, 햄릿",
    "“인간은 자신이 바라는 것을 사랑한다.” – 알베르 카뮈",
    "“사랑은 모든 것을 견디고, 믿고, 바란다.” – 바울",
    "“세상은 두 가지로 이루어져 있다. 선과 악.” – 괴테",
    "“바람이 분다. 살아야겠다.” – 미야자와 겐지",
    "“인간은 자유롭게 태어났으나 어디서나 속박되어 있다.” – 루소",
    "“나는 나를 믿는다, 그러므로 나는 존재한다.” – 데카르트",
    "“모든 위대한 글은 약간의 광기를 지닌다.” – 아리스토텔레스",
    "“나는 별을 바라본다, 그러므로 나는 꿈꾼다.” – 릴케",
    "“우리는 결국 우리의 선택으로 정의된다.” – 카뮈",
    "“단어는 인간의 가장 강력한 무기다.” – 키플링",
    "“슬픔은 인생의 필수 조건이다.” – 톨스토이",
    "“행복은 늘 가까이에 있다.” – 오스카 와일드",
    "“그대 마음의 어둠 속에서 별을 찾아라.” – 니체",
    "“모든 인간은 죽는다, 그러나 모든 인간이 살아있는 것은 아니다.” – 셰익스피어",
    "“나는 나의 길을 쓸 것이다.” – 무라카미 하루키",
    "“고독 속에서야 비로소 나는 나를 만난다.” – 보들레르",
    "“삶은 결국 이야기다.” – 체호프",
    "“사랑이 없다면 글도 없다.” – 릴케",
    "“희망은 인간을 지탱하는 힘이다.” – 괴테",
    "“펜 끝에서 세상은 다시 태어난다.” – 톨스토이",
    "“별을 바라보며 나는 꿈을 쓴다.” – 슈테판 츠바이크"
]

# -----------------------
# 기분 옵션
# -----------------------
moods = ["행복 😊", "우울 🌑", "분노 🔥", "차분 🍃", "창작의 불꽃 ✨"]

# -----------------------
# 세션 상태
# -----------------------
if "saved_quotes" not in st.session_state:
    st.session_state.saved_quotes = []
if "current_quote" not in st.session_state:
    st.session_state.current_quote = None
if "current_line" not in st.session_state:
    st.session_state.current_line = None

# -----------------------
# 타이틀
# -----------------------
st.title("🌌 작가의 영감 노트 ✨")
st.markdown("오늘의 기분에 맞는 명언과 문학 명대사를 만나고, 나만의 글과 태그로 기록하세요.")

# -----------------------
# 사이드바: 오늘의 기분
# -----------------------
st.sidebar.header("🎭 오늘의 기분 선택")
today_mood = st.sidebar.radio("기분:", moods)

# -----------------------
# 명언 / 문학 명대사 버튼
# -----------------------
col1, col2 = st.columns(2)
with col1:
    if st.button("오늘의 명언 뽑기"):
        filtered = [q for q in quotes if q["mood"] in today_mood]
        if filtered:
            st.session_state.current_quote = random.choice(filtered)["text"]
        else:
            st.session_state.current_quote = "해당 기분에 맞는 명언이 아직 준비되지 않았습니다."
with col2:
    if st.button("문학 명대사 뽑기"):
        st.session_state.current_line = random.choice(literary_quotes)

# -----------------------
# 출력
# -----------------------
if st.session_state.current_quote:
    st.subheader("📖 오늘의 명언")
    st.info(st.session_state.current_quote)

if st.session_state.current_line:
    st.subheader("🎬 문학 명대사")
    st.info(st.session_state.current_line)

# -----------------------
# 글쓰기 + 태그
# -----------------------
st.header("🖋️ 나의 글쓰기")
user_text = st.text_area("오늘 떠오른 글귀, 아이디어, 문장들을 적어보세요.")

st.subheader("📌 태그 달기")
tags = st.text_input("태그를 입력하세요 (쉼표로 구분)")

if st.button("💾 저장하기"):
    if user_text.strip() == "":
        st.warning("내용을 먼저 입력해주세요!")
    else:
        # 어떤 글귀인지 구분
        source = "명언" if st.session_state.current_quote else "문학 명대사"
        st.session_state.saved_quotes.append(
            {"source": source, "content": user_text, "tags": tags, "mood": today_mood}
        )
        st.success(f"✅ 저장 완료!\n**출처:** {source}\n**태그:** {tags if tags else '없음'}\n**기분:** {today_mood}")

# -----------------------
# 저장된 글 보기
# -----------------------
if st.session_state.saved_quotes:
    st.subheader("📚 나의 영감 저장소")
    for idx, item in enumerate(st.session_state.saved_quotes,
