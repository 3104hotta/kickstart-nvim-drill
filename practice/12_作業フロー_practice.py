# 練習用ファイル: 12_作業フロー_practice.py


def calculate_tax(amount: float) -> float:
    """税額を計算する。"""
    return amount * 0.1


def calculate_total(amount: float) -> float:
    """税込み合計を計算する。"""
    tax = calculate_tax(amount)
    return amount + tax


def legacy_api(endpoint: str, data: dict) -> dict:
    """旧APIを呼び出す。"""
    print(f"[legacy_api] {endpoint}: {data}")
    return {"status": "ok"}


def fetch_user(user_id: int) -> dict:
    """ユーザー情報を取得する。"""
    result = legacy_api(f"/users/{user_id}", {})
    return result


def update_user(user_id: int, data: dict) -> dict:
    """ユーザー情報を更新する。"""
    result = legacy_api(f"/users/{user_id}", data)
    return result


def main():
    total = calculate_total(1000)
    print(f"合計: {total}")

    user = fetch_user(1)
    update_user(1, {"name": "新しい名前"})
    print(user)


if __name__ == "__main__":
    main()
