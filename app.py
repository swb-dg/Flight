
import streamlit as st
import json
import os
from user_config import get_user_config
from check_ticket import check_ticket
from send_alert import send_email_alert

STOP_LIST_PATH = "stop_list.json"

def save_to_stop_list(email):
    if not os.path.exists(STOP_LIST_PATH):
        with open(STOP_LIST_PATH, "w") as f:
            json.dump({"stopped_emails": []}, f)

    with open(STOP_LIST_PATH, "r") as f:
        data = json.load(f)

    if email not in data["stopped_emails"]:
        data["stopped_emails"].append(email)
        with open(STOP_LIST_PATH, "w") as f:
            json.dump(data, f)

# 탭 구성
tab1, tab2 = st.tabs(["항공권 등록", "알림 중단 요청"])

with tab1:
    st.title("✈️ 항공권 알림 등록")
    airports = ["GMP", "ICN", "CJU"]
    col1, col2 = st.columns(2)
    with col1:
        departure = st.selectbox("출발 공항", airports)
    with col2:
        arrival = st.selectbox("도착 공항", airports)

    col3, col4 = st.columns(2)
    with col3:
        start_date = st.date_input("탑승 시작일")
        start_time = st.time_input("탑승 시작 시간", step=3600)
    with col4:
        end_date = st.date_input("탑승 종료일")
        end_time = st.time_input("탑승 종료 시간", step=3600)

    email = st.text_input("이메일 주소")

    if st.button("등록"):
        st.session_state["user_input"] = {
            "departure": departure,
            "arrival": arrival,
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time,
            "email": email
        }
        st.success("등록이 완료되었습니다.")
        
        try:
            config = get_user_config()
            st.info("🔍 항공편 확인 중...")
            matching_flights = check_ticket(config)
            st.write("✅ 확인된 항공편:", matching_flights)
            if matching_flights:
                send_email_alert(config, matching_flights)
                st.success("📩 알림 이메일이 전송되었습니다.")
            else:
                st.warning("조건에 맞는 예약 가능 항공편이 없습니다.")
        except Exception as e:
            st.error(f"❌ 처리 중 오류 발생: {e}")

with tab2:
    st.title("🔕 알림 중단 요청")
    stop_email = st.text_input("중단할 이메일 주소를 입력하세요", key="stop_email")

    if st.button("알림 중단하기"):
        if "@" not in stop_email:
            st.warning("유효한 이메일을 입력하세요.")
        else:
            save_to_stop_list(stop_email)
            st.success(f"{stop_email} 에 대한 알림이 중단되었습니다.")
