import streamlit as st

# ------------------------
# 맞춤법 퀴즈 데이터 (총 12문제)
# ------------------------
quiz_data = [
    {"question": "다음 중 올바른 맞춤법은?", "options": ["안 되", "안돼", "않돼"], "answer": "안돼"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["금세", "금새", "금"], "answer": "금새"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["맞히다", "맞추다", "마추다"], "answer": "맞히다"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["왠지", "웬지", "왠진"], "answer": "왠지"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["깨끄시", "깨끗히", "깨끗이"], "answer": "깨끗이"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["설겆이", "설겆지", "설거지"], "answer": "넓적하다"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["어떻해", "어떡해", "어떠케"], "answer": "까닭"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["며칠", "몇 일", "몇"], "answer": "하다"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["왼만하면", "왠만하면", "웬만하"], "answer": "웬만하"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["오랫만에", "오랜만에", "오래만에"], "answer": "오랜만"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["잠갔다", "잠궜다", "잠깃"], "answer": "가엾다"},
    {"question": "다음 중 올바른 맞춤법은?", "options": ["내꺼", "내거", "내 거"], "answer": "내거"},
]

# ------------------------
# 앱 제목 & 소개
# ------------------------
st.title("✏️ 헷갈리기 쉬운 국어 맞춤법 퀴즈")
st.write("헷갈리기 쉬운 맞춤법 문제를 풀어보세요! ✅🎉")

# ------------------------
# 세션 상태 초기화
# ------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "wrong_list" not in st.session_state:
    st.session_state.wrong_list = []

# ------------------------
# 문제 풀이 구간
# ------------------------
if st.session_state.current_q < len(quiz_data):
    q = quiz_data[st.session_state.current_q]
    st.subheader(f"문제 {st.session_state.current_q + 1}")
    st.write(q["question"])
    
    choice = st.radio("보기", q["options"], index=None)

    if st.button("정답 확인"):
        if choice == q["answer"]:
            st.success("정답입니다! 🎉")
            st.balloons()  # 🎈 정답 효과
            st.session_state.score += 1
        else:
            st.error(f"틀렸습니다 😭 정답은 👉 {q['answer']}")
            st.session_state.wrong_list.append(q)
        
        st.session_state.current_q += 1
        st.rerun()

# ------------------------
# 퀴즈 종료 후 결과 출력
# ------------------------
else:
    st.subheader("📊 퀴즈 완료! 성적표")
    st.write(f"총 문제 수: {len(quiz_data)}")
    st.write(f"맞힌 문제 수: {st.session_state.score}")
    st.write(f"틀린 문제 수: {len(quiz_data) - st.session_state.score}")
    
    # 성적 등급 안내
    score_rate = st.session_state.score / len(quiz_data) * 100
    if score_rate == 100:
        st.success("🎉 완벽해요! 모든 문제를 맞췄습니다 👏")
    elif score_rate >= 70:
        st.info("👍 잘했어요! 조금만 더 연습하면 완벽해질 거예요!")
    else:
        st.warning("📖 조금 더 공부가 필요해요. 오답노트를 확인해 보세요!")

    # 오답노트
    if st.session_state.wrong_list:
        st.write("📘 오답노트")
        for w in st.session_state.wrong_list:
            st.write(f"- {w['question']} (정답: {w['answer']})")

    # 다시 풀기 버튼
    if st.button("🔄 다시 풀기"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.session_state.wrong_list = []
        st.rerun()
