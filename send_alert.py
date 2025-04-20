# send_alert.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(config, matching_flights):
    """
    매칭된 항공편 정보를 사용자에게 이메일로 전송합니다.
    
    Parameters:
    - config: dict, get_user_config()에서 반환된 사용자 입력값
    - matching_flights: list of dict, 항공편 확인 모듈에서 필터링된 항공편 리스트
    """
    if not matching_flights:
        return  # 알림 보낼 내용이 없으면 종료

    sender_email = "YOUR_EMAIL@gmail.com"         # 발신자 이메일
    sender_password = "YOUR_APP_PASSWORD"         # Gmail 앱 비밀번호
    receiver_email = config["email"]

    subject = "✈️ 항공권 알림 - 예매 가능 항공편 발견!"
    
    body = "다음 항공편이 예매 가능 상태로 확인되었습니다:\n\n"
    for flight in matching_flights:
        body += f"- {flight['airline']} {flight['flight_number']} | {flight['depart_time']} → {flight['arrive_time']} | 가격: {flight['price']}원\n"

    body += "\n빠르게 확인하세요! (본 메일은 자동 발송입니다.)"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"[ALERT SENT] 항공편 알림을 {receiver_email}로 전송했습니다.")
    except Exception as e:
        print(f"[ERROR] 이메일 전송 실패: {e}")
