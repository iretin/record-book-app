import streamlit as st

st.set_page_config(page_title="생활기록부 작성기", page_icon="📋")

st.title("📋 생활기록부 작성기")

# ✅ 과목 선택 드롭다운
subject = st.selectbox(
    "과목 선택",
    ["국어", "수학", "영어", "사회", "과학", "기술가정", "도덕", "체육"]
)

name = st.text_input("이름")
grade = st.text_input("학년/반/번호")
birth = st.date_input("생년월일")
talent = st.text_area("특기사항", height=100)
opinion = st.text_area("담임의견", height=100)
dream = st.text_input("진로희망")

if st.button("💾 저장하기"):
    content = f"""[생활기록부 - {subject}]
이름: {name}
학년/반/번호: {grade}
생년월일: {birth}

[특기사항]
{talent}

[담임의견]
{opinion}

[진로희망]
{dream}
"""
    file_name = f"{name}_{subject}_생활기록부.txt"
    st.download_button("📄 다운로드", content, file_name=file_name)
    st.success(f"{subject} 생활기록부가 저장되었습니다!")
