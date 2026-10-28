# 도서관 대출 시스템

바이브코딩 실기 시험 과제입니다. 문제와 규칙은 [PROBLEM.md](PROBLEM.md)에 있습니다.

## 구성

| 파일 | 설명 |
|---|---|
| `solution.py` | `LibraryLoan` 클래스 — 대출 규칙 전체 (`borrow`, `return_book`, `get_loans`) |
| `index.html` | 웹페이지. [Pyodide](https://pyodide.org)로 브라우저 안에서 `solution.py`를 그대로 불러와 실행 |
| `check.py` | 샘플 테스트 5개 (수정 금지) |
| `PROBLEM.md` | 문제지 |

- 웹은 대출 규칙을 따로 갖고 있지 않습니다. 입력을 `solution.py`에 넘기고 결과만 보여줍니다.
  - 웹에서 하는 입력 정리: 책 번호는 앞뒤 공백 제거 + 대문자 변환, 이름은 앞뒤 공백 제거, 날짜는 글자를 숫자(정수/소수)로만 변환
- 대출 기록은 방문자마다 브라우저 안에 따로 저장됩니다. 새로고침하거나 「처음 상태로 초기화」를 누르면 처음 상태로 돌아갑니다.

## 문제지에 없는 예외 처리 (확인 후 적용)

- 이름이 문자열이 아니거나 빈 문자열/공백뿐이면 거절 (`borrow` → `False`, `return_book` → `-1`, `get_loans` → `[]`)
- 이름·책 번호는 정확히 일치해야 같은 것으로 봄 (`"b001"`, `" B001"`, `1`은 없는 책)
- 없는 책 번호로 반납, 반납 날짜가 `True`/`False` → `-1`
- 날짜가 과거로 되돌아가는 입력은 따로 막지 않음

## 실행

```bash
# 샘플 테스트
python check.py

# 웹페이지 (fetch를 쓰므로 파일을 직접 열지 말고 로컬 서버로 열기)
python -m http.server 8000
# → http://localhost:8000
```

## 배포

GitHub Pages (Settings → Pages → Deploy from a branch → `main` / `(root)`).
`solution.py`나 `index.html`을 고친 뒤 push하면 몇 분 안에 반영됩니다.
