
from datetime import datetime

def get_user_config(raw_input: dict) -> dict:
    """
    사용자의 입력값을 구조화하여 딕셔너리로 반환
    필수 필드 누락, 유효하지 않은 값 등에 대한 기본 검증 포함
    """
    # === 1. 필수 필드 확인 ===
    required_fields = ["departure", "arrival", "start_date", "end_date", "start_time", "end_time", "email"]
    for field in required_fields:
        if field not in raw_input:
            raise ValueError(f"입력 누락: {field}")

    # === 2. 출/도착 공항 동일 체크 ===
    if raw_input["departure"] == raw_input["arrival"]:
        raise ValueError("출발지와 도착지가 동일할 수 없습니다.")

    # === 3. 이메일 간단 검증 ===
    if "@" not in raw_input["email"]:
        raise ValueError("유효하지 않은 이메일입니다.")

    # === 4. 날짜 + 시각 합치기 ===
    start_datetime = datetime.combine(raw_input["start_date"], raw_input["start_time"])
    end_datetime = datetime.combine(raw_input["end_date"], raw_input["end_time"])

    # === 5. 시작 > 종료일 경우 → 자동 반전 ===
    if start_datetime > end_datetime:
        start_datetime, end_datetime = end_datetime, start_datetime

    # === 6. 최종 구성 ===
    return {
        "departure": raw_input["departure"],
        "arrival": raw_input["arrival"],
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "email": raw_input["email"]
    }
