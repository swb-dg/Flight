# ✈️ 항공권 취소표 알림 시스템

**김포/인천 ↔ 제주 항공권**이 매진된 후, **다시 예약 가능해졌을 때 실시간으로 알림을 보내는 웹앱**입니다.  
Streamlit 기반 UI로 사용자 입력을 받고, 네이버 항공권 API를 통해 예약 가능 상태를 실시간 감시합니다.

> ❌ 자동 예매는 하지 않으며  
> ✔️ 알림 전송에 최적화된 구조입니다.

---

## 🔧 기능 요약

- ✅ 사용자 입력 UI (출/도착지, 날짜/시간대, 이메일)
- ✅ 항공편 조회 (Naver 비공식 API 활용)
- ✅ 예약 가능 항공편 필터링 (시간 조건 포함)
- ✅ 이메일 알림 발송 (Gmail SMTP)
- ✅ 감시 루프 및 중복 알림 방지
- ✅ Streamlit Cloud 배포 완료

---

## 🧱 주요 기술 스택

| 구성 요소 | 설명 |
|-----------|------|
| Python    | 전체 모듈 구현 |
| Streamlit | 사용자 UI 구현 및 배포 |
| requests  | 네이버 항공편 XHR API 호출 |
| smtplib   | 이메일 발송 |
| schedule/threading | 감시 루프 구성 |

---

## 🗂 파일 구조

| 파일명 | 설명 |
|--------|------|
| `app.py` | 사용자 UI 진입점 |
| `user_config.py` | 입력값 구조화 및 유효성 검사 |
| `ticket_checker.py` | 항공편 필터링 로직 |
| `email_sender.py` | 이메일 템플릿 및 전송 모듈 |
| `monitor.py` | 감시 루프 및 중복 알림 방지 |
| `requirements.txt` | 필요한 라이브러리 목록 |
| `.streamlit/config.toml` | UI 기본 설정 |
| `GPT_PROJECT_GUIDELINES.md` | 프로젝트 전체 구조 및 단계별 메모 |

---

## 🚀 배포 방법

본 프로젝트는 GitHub와 Streamlit Cloud를 연동하여 배포됩니다.

1. GitHub에 커밋/푸시 완료
2. [Streamlit Cloud](https://streamlit.io/cloud) 접속
3. "New app" 클릭 후:
   - Repository: `your-username/your-repo`
   - Branch: `main`
   - File: `app.py`
4. Deploy 클릭 → 웹에서 사용 가능

---

## 📬 사용 시 주의사항

- 이메일 발송을 위해 Gmail 계정 설정 필요 (앱 비밀번호 사용)
- 현재는 단일 사용자 기준 구조이며, 다중 사용자 확장은 예정되어 있음
- 예약 감지는 `출발일 + 항공편명 + 출발시간` 기준으로 중복 방지됨

---

## 📌 향후 확장 계획

- SMS 알림 (Solapi 등 연동)
- 사용자 조건 저장 (DB 또는 JSON)
- 감시 주기 사용자 설정
- UI 테마 업그레이드
- 다중 날짜 모니터링

---

## 👤 개발자

- 기획/구현: [민준희: jmin9822]
- 협업: ChatGPT