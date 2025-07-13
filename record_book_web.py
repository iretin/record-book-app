import streamlit as st

# ✅ 로그인 성공 시 보여줄 내용
st.set_page_config(page_title="생활기록부 작성기", page_icon="📋")
st.title("📋 생활기록부 작성기")

# ✅ 간단한 로그인 시스템
def check_password():
    st.title("🔐 로그인")
    password = st.text_input("비밀번호를 입력하세요", type="password")
    if password == "1234":  # 원하는 비밀번호로 바꿔도 됨
        st.session_state["authenticated"] = True
    elif password:
        st.error("비밀번호가 틀렸습니다.")

# ✅ 로그인 상태 체크
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    check_password()
    st.stop()

subject = st.selectbox("과목 선택", ["국어", "수학", "영어", "사회", "과학", "기술가정", "도덕", "체육"])
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
