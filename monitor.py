import time
import schedule
from user_config import get_user_config
from check_ticket import check_ticket
from send_alert import send_email_alert

# 중복 알림 방지를 위한 캐시
sent_flights = set()

def monitor():
    try:
        config = get_user_config()
        matching_flights = check_ticket(config)
    except Exception as e:
        print(f"[ERROR] 데이터 조회 중 오류 발생: {e}")
        return

    new_flights = []
    for flight in matching_flights:
        # 날짜 포함하여 중복 방지 ID 구성
        flight_id = f"{flight['date']}_{flight['flight_number']}_{flight['depart_time']}"
        if flight_id not in sent_flights:
            new_flights.append(flight)
            sent_flights.add(flight_id)

    if new_flights:
        print(f"[INFO] 새로운 항공편 {len(new_flights)}개 발견 → 알림 전송")
        try:
            send_email_alert(config, new_flights)
        except Exception as e:
            print(f"[ERROR] 이메일 발송 중 오류 발생: {e}")
    else:
        print("[INFO] 새로운 항공편 없음")

# 스케줄 등록 (기본: 10분 주기)
schedule.every(10).minutes.do(monitor)

if __name__ == "__main__":
    # 수동 테스트용 단발 실행
    print("[TEST] monitor() 1회 실행")
    monitor()

    # 주기적 감시 루프 실행
    print("[LOOP] 감시 루프 시작 (10분 간격)")
    while True:
        schedule.run_pending()
        time.sleep(1)

# TODO: 다중 사용자 구조로의 확장 고려 필요 (user_config 다중 처리, 캐시 분리 등)