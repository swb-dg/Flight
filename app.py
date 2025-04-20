import streamlit as st
from datetime import date, time, timedelta

# 제목
st.title("✈️ 항공권 알림 등록")

# === 1. 공항 선택 ===
airport_options = ["GMP", "ICN", "CJU"]

col1, col2 = st.columns(2)
with col1:
    departure = st.selectbox("출발 공항", airport_options, index=0)
with col2:
    arrival = st.selectbox("도착 공항", airport_options, index=2)

# === 2. 탑승 날짜 및 시각 ===
today = date.today()
min_date = today + timedelta(days=1)

col3, col4 = st.columns(2)
with col3:
    start_date = st.date_input("탑승 시작일", min_value=min_date, value=min_date)
with col4:
    end_date = st.date_input("탑승 종료일", min_value=min_date, value=min_date)

# 1시간 단위 시간 선택
hour_options = [time(h, 0) for h in range(0, 24)]

def format_time(t):
    return t.strftime("%H:%M")

col5, col6 = st.columns(2)
with col5:
    start_time = st.selectbox("시작 시각", hour_options, index=8, format_func=format_time)
with col6:
    end_time = st.selectbox("종료 시각", hour_options, index=20, format_func=format_time)

# 자동 반전 처리
if (start_date, start_time) > (end_date, end_time):
    start_date, end_date = end_date, start_date
    start_time, end_time = end_time, start_time
    st.info("시작일/시각이 종료일/시각보다 나중이어서 자동으로 순서를 반전했어요.")

# === 3. 이메일 + 등록 버튼 ===
email = st.text_input("📧 이메일 주소를 입력하세요")

if st.button("등록"):
    if "@" not in email or "." not in email:
        st.error("유효한 이메일 주소를 입력해주세요.")
    else:
        st.session_state["user_input"] = {
            "departure": departure,
            "arrival": arrival,
            "start_date": start_date,
            "end_date": end_date,
            "start_time": start_time.strftime("%H:%M"),
            "end_time": end_time.strftime("%H:%M"),
            "email": email
        }
        st.success("입력값이 성공적으로 등록되었습니다!")
        st.write("📝 입력 내용:", st.session_state["user_input"])