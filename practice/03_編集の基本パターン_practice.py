# 練習用ファイル: 03_編集の基本パターン_practice.py


def old_function(x: int) -> int:
    """2乗を返す（関数名が古い）。"""
    return "placeholder"


def calculate(a: int, b: int) -> int:
    """合計を計算する。"""
    result = calculate(100, 200)
    return a + b


greeting = "Hello, World!"
old_name = "legacy"
unused_line = "この行は不要です"

items = ["apple", "banana", "cherry", "REMOVE_ME"]

config = {
    "debug": True,
    "timeout": 30,
    "retries": 3,
}


def process_data(input_data, verbose=True):
    """データを処理する。"""
    if verbose:
        print(f"処理中: {input_data}")
    return input_data


# TODO: remove this later
if __name__ == "__main__":
    process_data(input_data, verbose=True)
