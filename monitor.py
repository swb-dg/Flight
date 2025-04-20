
import time
import json
from user_config import get_user_config
from check_ticket import check_ticket
from send_alert import send_email_alert

STOP_LIST_PATH = "stop_list.json"

def load_stopped_emails():
    try:
        with open(STOP_LIST_PATH, "r") as f:
            data = json.load(f)
            return data.get("stopped_emails", [])
    except FileNotFoundError:
        return []

def monitor():
    sent_flights = set()
    while True:
        config = get_user_config()
        stopped_emails = load_stopped_emails()

        if config["email"] in stopped_emails:
            print(f"[INFO] {config['email']} 알림 중단 상태. 스킵합니다.")
            time.sleep(600)
            continue

        print("[INFO] 항공권 확인 중...")
        flights = check_ticket(config)

        new_flights = []
        for flight in flights:
            identifier = f"{flight['date']}_{flight['flight_number']}_{flight['depart_time']}"
            if identifier not in sent_flights:
                new_flights.append(flight)
                sent_flights.add(identifier)

        if new_flights:
            print(f"[INFO] 새로운 항공편 {len(new_flights)}건 발견, 이메일 발송 중...")
            send_email_alert(config, new_flights)
        else:
            print("[INFO] 새로운 항공편 없음.")

        time.sleep(600)

if __name__ == "__main__":
    monitor()
