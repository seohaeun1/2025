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
# 명언 데이터 (기분별)
# -----------------------
quotes = {
    "행복": [
        "상상력은 지식보다 더 중요하다. – 아인슈타인",
        "한 줄의 시가 인생을 바꿀 수 있다. – 오든",
        "펜은 칼보다 강하다. – 키플링"
    ],
    "슬픔": [
        "문학은 인간의 내면을 비추는 거울이다. – 톨스토이",
        "소설은 인간에 관한 진실을 드러내는 장치다. – 카프카",
        "글을 쓰는 일은 고통이지만, 쓰지 않는 것은 더 큰 고통이다. – 무라카미 하루키"
    ],
    "분노": [
        "창작은 혼돈에서 질서를 만들어내는 일이다. – 니체",
        "모든 위대한 작가는 조금씩 미쳤다. – 아리스토텔레스",
        "책은 도끼다. 우리의 얼어붙은 마음의 바다를 깨뜨리는. – 카프카"
    ],
    "차분": [
        "삶은 짧고 예술은 길다. – 히포크라테스",
        "시인은 진실을 말하고, 소설가는 그 진실을 증명한다. – 무라카미 하루키",
        "언어는 존재의 집이다. – 하이데거"
    ],
    "창작의 불꽃": [
        "진정한 작가는 말하지 못하는 것을 쓰는 사람이다. – 사르트르",
        "상처는 글로써 치유된다. – 셰익스피어",
        "위대한 글은 늘 작가 자신을 넘어선다. – 버지니아 울프"
    ]
}

# -----------------------
# 문학 명대사 (실제 소설/시 구절)
# -----------------------
literary_quotes = [
    "“모든 행복한 가정은 서로 닮았고, 불행한 가정은 제각각의 이유로 불행하다.” – 톨스토이, 안나 카레니나",
    "“죽느냐 사느냐, 그것이 문제로다.” – 셰익스피어, 햄릿",
    "“바람이 분다. 살아야겠다.” – 미야자와 겐지",
    "“나는 고독 속에서 나를 만난다.” – 보들레르, 악의 꽃",
    "“슬픔이 지나가면, 사랑이 남는다.” – 괴테, 젊은 베르테르의 슬픔",
    "“별을 바라보며 나는 꿈을 쓴다.” – 릴케, 말테의 수기",
    "“인생은 우리가 이야기하는 것과 같다.” – 체호프, 체리밭",
    "“사랑이 없다면 글도 없다.” – 릴케, 독일어 시집",
    "“모든 인간은 자유롭게 태어났다, 그러나 어디서나 속박되어 있다.” – 루소, 사회계약론",
    "“나는 나의 길을 쓰겠다.” – 무라카미 하루키, 해변의 카프카",
    "“그대 마음의 어둠 속에서 별을 찾아라.” – 니체, 차라투스트라는 이렇게 말했다",
    "“오늘 내가 사는 것은 어제 죽은 이들이 살고 싶었던 내일이다.” – 투르게네프, 아버지와 아들",
    "“가장 어두운 밤이 지나야 해가 뜬다.” – 빅토르 위고, 레 미제라블",
    "“행복은 늘 가까이에 있다.” – 오스카 와일드, 도리언 그레이의 초상",
    "“나는 별을 바라본다. 그러므로 나는 꿈꾼다.” – 릴케, 말테의 수기"
]

# -----------------------
# 기분 옵션
# -----------------------
moods = ["행복", "슬픔", "분노", "차분", "창작의 불꽃"]

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
        st.session_state.current_quote = random.choice(quotes[today_mood])
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
    for idx, item in enumerate(st.session_state.saved_quotes, 1):
        st.write(f"**{idx}. ({item['source']})** {item['content']}")
        st.write(f"태그: {item['tags']} | 기분: {item['mood']}")
        st.markdown("---")
