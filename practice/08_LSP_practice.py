# 練習用ファイル: 08_LSP_practice.py
# LSP の練習用。pyright / basedpyright が起動していることを確認してください


class UserProfile:
    """ユーザープロフィールを表すクラス。"""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"こんにちは、{self.name}さん（{self.age}歳）"


def calculate_area(width: float, height: float) -> float:
    """長方形の面積を計算する。

    Args:
        width: 幅
        height: 高さ

    Returns:
        面積
    """
    return width * height


def calculate_volume(width: float, height: float, depth: float) -> float:
    """直方体の体積を計算する。"""
    return calculate_area(width, height) * depth


old_variable = 42
temp_value = calculate_area(10.0, 5.0)


def process_user(profile: UserProfile) -> str:
    """ユーザープロフィールを処理する。"""
    return profile.greet()


def main() -> None:
    user = UserProfile("太郎", 30)
    result = process_user(user)
    print(result)

    area = calculate_area(3.0, 4.0)
    volume = calculate_volume(3.0, 4.0, 5.0)
    print(f"面積: {area}, 体積: {volume}")
    print(f"変数: {old_variable}, 計算結果: {temp_value}")


if __name__ == "__main__":
    main()
