# 練習用ファイル: 04_繰り返しの3種_practice.py


# --- Q1 用: DEBUG行を削除 ---
def process():
    # DEBUG: step 1
    result = fetch_data()
    # DEBUG: step 2
    cleaned = clean(result)
    # DEBUG: step 3
    return cleaned


# --- Q2 用: pending → done ---
task_a = {"name": "タスクA", "status": "pending"}
task_b = {"name": "タスクB", "status": "pending"}
task_c = {"name": "タスクC", "status": "pending"}


# --- Q4 用: マクロ練習 ---
log_entries = [
    "event_login",
    "event_logout",
    "event_purchase",
    "event_error",
]

extra_entries = [
    "event_signup",
    "event_delete",
]


# --- Q6 用: section → chapter ---
# section_1
# section_2
# section_3
# section_4
# section_5


# --- Q7 用: FIXME削除 ---
def calculate(x, y):
    # FIXME: バリデーション未実装
    a = old_api_call()
    # FIXME: エラーハンドリングが必要
    b = old_api_call()
    # FIXME: ログ出力を追加する
    c = old_api_call()
    # FIXME: テストを書く
    # FIXME: ドキュメントを更新する
    return a + b + c
