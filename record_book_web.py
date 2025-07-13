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

import streamlit as st

st.set_page_config(page_title="생활기록부 작성기", page_icon="📋")

st.title("📋 생활기록부 작성기")

# 1. 수업선택 (직접 입력 가능)
subject_input = st.text_input("수업 선택 (직접 입력)")

# 2. 학생선택 (직접 입력 가능)
student_input = st.text_input("학생 이름 입력")

# 3. 내용 입력
content_input = st.text_area("내용 입력", height=200)

# 4. 저장하기 버튼
if st.button("💾 저장하기"):
    if not subject_input or not student_input or not content_input:
        st.error("모든 항목을 입력해주세요.")
    else:
        file_content = f"[생활기록부]\n수업: {subject_input}\n학생: {student_input}\n\n내용:\n{content_input}"
        file_name = f"{student_input}_{subject_input}_생활기록부.txt"
        st.download_button("📄 텍스트 파일 다운로드", file_content, file_name=file_name)
        st.success(f"'{file_name}' 저장 준비 완료!")
