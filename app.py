import streamlit as st
import random

# ---------------------------
# 데이터 준비
# ---------------------------
quotes = [
    "글쓰기는 자기 자신과의 대화다. - 헤밍웨이",
    "상상력은 지식보다 더 중요하다. - 아인슈타인",
    "오늘 할 수 있는 일을 내일로 미루지 말라. - 벤자민 프랭클린",
    "삶이 있는 한 희망은 있다. - 키케로",
    "예술은 거짓을 말하지만 그 속에 진실이 있다. - 파블로 피카소",
    "작가는 세상을 두 번 산다. - 나탈리 골드버그",
]

literary_lines = [
    "우리는 모두 별이자 동시에 진흙이다. - 오스카 와일드",
    "내 안에 다른 내가 있다. - 김소월",
    "사랑이 끝나는 순간에도 사랑은 있었다. - 알베르 카뮈",
    "그는 바다를 보았다. 그것은 푸르고도 슬펐다. - 헤밍웨이",
    "나는 내 운명의 주인이며, 내 영혼의 선장이리라. - 윌리엄 어니스트 헨리",
    "그대의 하루가 눈부시길, 비록 세상이 어둡다 해도. - 미상",
    "모든 진정한 삶은 만남이다. - 마르틴 부버",
    "눈 오는 날은 너를 더 그리워한다. - 장석주",
    "인생은 짧고 예술은 길다. - 히포크라테스",
]

# ---------------------------
# UI 꾸미기
# ---------------------------
st.set_page_config(
    page_title="✨ 낭만 작가의 방 ✨",
    page_icon="📚",
    layout="centered"
)

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #1e1e2f, #3c1053, #ad5389);
        color: #f0f0f0;
        font-family: "Helvetica Neue", sans-serif;
    }
    .big-title {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #ffd700;
        text-shadow: 2px 2px #000;
    }
    .sub {
        font-size: 20px;
        text-align: center;
        color: #ffddf4;
        margin-bottom: 30px;
    }
    .quote-box {
        background: rgba(255,255,255,0.1);
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        font-style: italic;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="big-title">📖 낭만 작가의 비밀 작업실</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">오늘도 글로 살아가는 너를 위하여 ✍️</div>', unsafe_allow_html=True)

# ---------------------------
# 오늘의 기분
# ---------------------------
st.header("🌈 오늘의 기분 선택")
mood = st.selectbox("오늘 기분은 어때?", ["행복 😊", "우울 😢", "분노 😡", "설렘 💖", "평온 🌿", "창의력 폭발 💡"])
st.success(f"오늘의 기분: {mood}")

# ---------------------------
# 오늘의 명언
# ---------------------------
st.header("💡 오늘의 명언")
st.markdown(f'<div class="quote-box">{random.choice(quotes)}</div>', unsafe_allow_html=True)

# ---------------------------
# 오늘의 문학 명대사
# ---------------------------
st.header("📚 오늘의 문학 명대사")
st.markdown(f'<div class="quote-box">{random.choice(literary_lines)}</div>', unsafe_allow_html=True)

# ---------------------------
# 내 글 작성 + 태그
# ---------------------------
st.header("📝 내 글 쓰기")
title = st.text_input("글 제목")
content = st.text_area("오늘 쓴 글을 여기에 적어봐")
tags = st.text_input("태그 (예: 사랑, 외로움, 희망)")

if st.button("저장하기"):
    st.success(f"'{title}' 저장됨! (태그: {tags})")
    st.info(content)
