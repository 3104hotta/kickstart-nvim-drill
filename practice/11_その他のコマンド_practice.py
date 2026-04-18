# 練習用ファイル: 11_その他のコマンド_practice.py


MAX_RETRIES = 3
TIMEOUT = 30
flag = false


# --- Q2 用: COMMENT_BLOCK ---
def slow_algorithm(data: list) -> list:
    result = []
    for item in data:
        result.append(item * 2)
    return result


# --- Q3 用: INDENT_SECTION ---
misaligned_code_a = 1
misaligned_code_b = 2
misaligned_code_c = 3


result = process(data)
status = "active"


# --- Q7 用: 行結合 ---
first_part = (
    "これは長い文字列の"
    "前半部分です"
)


# --- Q10 用: コメントトグル ---
todo_list = [
    "タスク1: ドキュメントを書く",
    "タスク2: テストを追加する",
    "タスク3: レビューを依頼する",
]


# --- Q4 用: BROKEN_INDENT ---
def broken_function():
    x = 1
    y = 2
    if x:
        z = x + y
    return z
