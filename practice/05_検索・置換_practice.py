# 練習用ファイル: 05_検索・置換_practice.py


# --- Q4 / Q8 用: old_user / v1 の置換 ---
def get_old_user(user_id: int):
    """old_user を取得する。"""
    old_user = fetch_from_db(user_id)
    return old_user


def update_old_user(old_user: dict, data: dict):
    """old_user を更新する。"""
    old_user.update(data)
    save_to_db(old_user)
    return old_user


API_VERSION = "v1"
ENDPOINT = "/api/v1/users"
BACKUP_ENDPOINT = "/api/v1/backup"


# --- Q5 用: TODO / DONE ---
def validate(username: str) -> bool:
    # TODO: 空文字チェックを追加
    if not username:
        return False
    # TODO: 最大長チェックを追加
    if len(username) > 50:
        return False
    # TODO: 使用禁止文字のチェックを追加
    return True


# --- Q6 用: REPLACE_SECTION ---
# REPLACE_SECTION
def calculate_price(quantity: int, price: float) -> float:
    total_price = quantity * price
    discounted_price = total_price * 0.9
    return discounted_price


def format_price(price: float) -> str:
    return f"¥{price:,.0f}"
# END_SECTION


# --- Q7 / Q3 用: username / user_id ---
def create_user(username: str, user_id: int) -> dict:
    """ユーザーを作成する。"""
    return {"username": username, "user_id": user_id}


def find_user(user_id: int) -> dict:
    """ユーザーを検索する。"""
    return {"user_id": user_id, "username": "sample"}


def delete_user(username: str, user_id: int) -> bool:
    """ユーザーを削除する。"""
    print(f"削除: {username} (id={user_id})")
    return True


# --- Q8 用: error_code ---
ERROR_MAP = {
    "error_code_404": "Not Found",
    "error_code_500": "Internal Server Error",
    "error_code_403": "Forbidden",
}


def handle_error(error_code: str) -> str:
    return ERROR_MAP.get(error_code, "Unknown Error")
