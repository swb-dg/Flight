# check_ticket.py

import requests
from datetime import datetime, timedelta
import time

def check_ticket(user_config: dict) -> list:
    """
    네이버 항공권 API를 통해 항공편 정보를 조회하고,
    예약 가능한 항공편을 조건에 맞게 필터링하여 반환합니다.
    """
    dep_code = user_config["departure"]
    arr_code = user_config["arrival"]
    start_dt = user_config["start_datetime"]
    end_dt = user_config["end_datetime"]

    results = []

    # 날짜 범위 생성
    curr_date = start_dt.date()
    end_date = end_dt.date()

    while curr_date <= end_date:
        # 날짜별 요청 URL 생성
        url = (
            "https://flight.naver.com/api/booking/availabilities"
            f"?fareType=Y&adt=1&depAirportCode={dep_code}&arrAirportCode={arr_code}&depDate={curr_date}"
        )

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            print(f"[ERROR] {curr_date} 항공편 조회 실패: {e}")
            curr_date += timedelta(days=1)
            time.sleep(0.5)
            continue

        # 응답 파싱
        for flight in data.get("flights", []):
            try:
                segments = flight["segments"][0]
                airline = segments["airline"]["name"]
                dep_time = datetime.fromisoformat(segments["departureDateTime"])
                arr_time = datetime.fromisoformat(segments["arrivalDateTime"])
                price = flight.get("price", {}).get("totalPrice", 0)
                status = flight.get("status")

                # 시간 필터링
                if not (start_dt <= dep_time <= end_dt):
                    continue

                # 예약 가능 여부 확인
                if status != "AVAILABLE":
                    continue

                results.append({
                    "airline": airline,
                    "departure_time": dep_time,
                    "arrival_time": arr_time,
                    "price": price,
                    "status": status
                })

            except Exception as e:
                print(f"[WARNING] 항공편 파싱 중 오류: {e}")
                continue

        curr_date += timedelta(days=1)
        time.sleep(0.5)  # 요청 간 간격 조절

    return results
