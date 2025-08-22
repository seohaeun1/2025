import streamlit as st

# 맞춤법 퀴즈 데이터
quiz_data = [
    {"question": "다음 중 올바른 맞춤법은?",
     "options": ["안 되", "안돼", "않돼"],
     "answer": "안돼"},
    
    {"question": "다음 중 올바른 맞춤법은?",
     "options": ["되려", "되이려", "되여"],
     "answer": "되려"},
    
    {"question": "다음 중 올바른 맞춤법은?",
     "options": ["맞히다", "맞추다", "마추다"],
     "answer": "맞히다"},
    
    {"question": "다음 중 올바른 맞춤법은?",
     "options": ["왠지", "웬지", "왠진"],
     "answer": "왠지"},
]

st.title("✏️ 국어 맞춤법 퀴즈")
st.write("헷갈리기 쉬운 맞춤법 문제를 풀어보세요!")

# 상태 저장 (점수, 진행상황)
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "wrong_list" not in st.session_state:
    st.session_state.wrong_list = []

# 현재 문제 불러오기
if st.session_state.current_q < len(quiz_data):
    q = quiz_data[st.session_state.current_q]
    st.subheader(f"문제 {st.session_state.current_q+1}")
    st.write(q["question"])
    
    choice = st.radio("보기", q["options"], index=None)

    if st.button("정답 확인"):
        if choice == q["answer"]:
            st.success("정답입니다! 🎉")
            st.balloons()
            st.session_state.score += 1
        else:
            st.error(f"틀렸습니다 😭 정답은 👉 {q['answer']}")
            st.session_state.wrong_list.append(q)
        
        st.session_state.current_q += 1
        st.experimental_rerun()

# 모든 문제 완료 후 결과 출력
else:
    st.subheader("퀴즈 완료!")
    st.write(f"최종 점수: **{st.session_state.score} / {len(quiz_data)}**")

    if st.session_state.wrong_list:
        st.write("📘 오답노트")
        for w in st.session_state.wrong_list:
            st.write(f"- {w['question']} (정답: {w['answer']})")
    else:
        st.success("완벽해요! 모든 문제를 맞췄습니다 👏")

    # 다시 풀기 버튼
    if st.button("다시 풀기"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.session_state.wrong_list = []
        st.experimental_rerun()
