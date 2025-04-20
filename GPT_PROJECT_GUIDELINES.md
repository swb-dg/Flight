## 6단계 메모

### ✅ 정리 요약

- `monitor.py` 파일 생성 및 감시 루프 구성 완료
- 주요 기능:
  - `get_user_config()` → `check_ticket()` → `send_email_alert()` 흐름을 10분 주기로 실행
  - 중복 알림 방지를 위해 `flight['date'] + flight['flight_number'] + flight['depart_time']` 기준으로 식별자 구성
  - 예외 발생 시 콘솔 출력으로 오류 확인 가능
- 단발 테스트 실행 (`__main__` 블록) 및 루프 시작 로그 출력 포함
- Git 커밋 예정: `"feat: 감시 루프 구성 및 중복 알림 방지 로직 추가"`

### 🧠 기억 보존 & 기준 유지 메모

- 단일 사용자 기준 구조로 구현되었으며, 추후 다중 사용자 확장 시 다음과 같은 리팩토링 필요:
  - `get_user_config()` → `get_all_user_configs()` 형태로 변경
  - 사용자별로 알림 캐시(`sent_flights`)를 분리하여 관리
- 항공편 식별자는 날짜 + 편명 + 출발시간으로 구성되어야 중복 여부를 정확히 판단할 수 있음
- 향후 `interval`을 유저 설정값으로 확장할 여지 있음
- 향후 SMS 전환 시에도 동일 로직 구조 활용 가능