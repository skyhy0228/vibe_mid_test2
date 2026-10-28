# 도서관 대출 시스템 — 아래 클래스를 완성하세요. (클래스·메서드 이름은 바꾸지 마세요)

BOOKS = ("B001", "B002", "B003", "B004", "B005")
LOAN_PERIOD = 14
MAX_LOANS = 3


def _is_valid_day(day):
    # bool은 int의 하위 타입이므로 따로 제외
    return isinstance(day, int) and not isinstance(day, bool) and day >= 1


def _is_valid_name(name):
    return isinstance(name, str) and name.strip() != ""


def _is_valid_book(book_id):
    return isinstance(book_id, str) and book_id in BOOKS


class LibraryLoan:
    def __init__(self):
        self._loans = {}        # book_id -> (name, 빌린 날)
        self._suspensions = {}  # name -> [(정지 시작일, 정지 마지막 날)] (양 끝 포함)

    def borrow(self, book_id, name, day):
        if not (_is_valid_book(book_id) and _is_valid_name(name) and _is_valid_day(day)):
            return False
        if book_id in self._loans:
            return False

        my_loans = [borrowed_day for (who, borrowed_day) in self._loans.values() if who == name]
        if len(my_loans) >= MAX_LOANS:
            return False
        if any(day > borrowed_day + LOAN_PERIOD for borrowed_day in my_loans):
            return False
        # 겹치는 정지 기간은 합쳐진 구간처럼 동작한다 (기간을 더하지 않음)
        if any(start <= day <= end for start, end in self._suspensions.get(name, [])):
            return False

        self._loans[book_id] = (name, day)
        return True

    def return_book(self, book_id, name, day):
        if not (_is_valid_book(book_id) and _is_valid_name(name) and _is_valid_day(day)):
            return -1
        loan = self._loans.get(book_id)
        if loan is None or loan[0] != name:
            return -1
        borrowed_day = loan[1]
        if day < borrowed_day:
            return -1

        overdue = max(0, day - (borrowed_day + LOAN_PERIOD))
        del self._loans[book_id]
        if overdue > 0:
            # 반납한 날부터 연체 일수만큼의 날 동안 대출 정지
            self._suspensions.setdefault(name, []).append((day, day + overdue - 1))
        return overdue

    def get_loans(self, name):
        loans = [
            (book_id, borrowed_day + LOAN_PERIOD)
            for book_id, (who, borrowed_day) in self._loans.items()
            if who == name
        ]
        return sorted(loans, key=lambda item: (item[1], item[0]))
