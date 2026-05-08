# 🎴 포켓몬 도감 프로젝트

포켓몬 1세대(151마리) 데이터를 조회하고, 중고나라에서 카드 시세를 크롤링하는 프로젝트입니다.
**CLI 버전**과 **Web(Flask) 버전** 두 가지 인터페이스를 제공합니다.

---

## 📁 프로젝트 구조

```
├── app.py              # Flask 웹 서버 (메인 백엔드)
├── CLI-read.py         # 터미널 기반 도감 탐색기
├── CLI-json.py         # PokeAPI 데이터 수집 및 캐시 생성
├── crawling.py         # 중고나라 카드 시세 크롤러
├── make_excel.py       # 크롤링 결과 엑셀 저장
├── pokemon_detail.py   # CLI 포켓몬 상세 보기
├── back_menu.py        # CLI 뒤로 가기 공통 유틸
├── pokemon_cache.json  # 포켓몬 데이터 캐시
├── favorites.json      # 즐겨찾기 저장 파일
├── requirements.txt    # 의존성 패키지 목록
└── templates/
    ├── index.html      # 포켓몬 목록 페이지
    ├── detail.html     # 포켓몬 상세 페이지
    └── favorites.html  # 즐겨찾기 페이지
```

---

## ⚙️ 설치 및 실행

**1. 패키지 설치**
```bash
pip install -r requirements.txt
```

**2. 포켓몬 데이터 수집** (최초 1회)
```bash
python CLI-json.py
```
> PokeAPI에서 151마리 데이터를 받아 `pokemon_cache.json`으로 저장합니다.

**3-A. 웹 버전 실행**
```bash
python app.py
```
> 브라우저에서 `http://127.0.0.1:5000` 접속

**3-B. CLI 버전 실행**
```bash
python CLI-read.py
```

---

## 🔧 주요 기능

| 기능 | CLI | Web |
|------|:---:|:---:|
| 타입별 포켓몬 조회 | ✅ | ✅ |
| 포켓몬 이름 검색 | ✅ | ✅ |
| 포켓몬 상세 정보 (기술, 진화) | ✅ | ✅ |
| 중고나라 카드 시세 조회 | ✅ | ✅ |
| 즐겨찾기 (최대 5마리) | ❌ | ✅ |
| 시세 결과 엑셀 저장 | ✅ | ✅ |

---

## 🗂️ 데이터 흐름

```
PokeAPI
   ↓ CLI-json.py (최초 1회 실행)
pokemon_cache.json
   ↓
app.py (Web) / CLI-read.py (Terminal)
   ↓
중고나라 crawling → 터미널 출력 or 엑셀 저장
```

---

## 📦 사용 라이브러리

- `requests` — API 및 크롤링 HTTP 요청
- `beautifulsoup4` — 중고나라 HTML 파싱
- `openpyxl` — 엑셀 파일 생성 및 편집
- `flask` — 웹 서버 프레임워크
