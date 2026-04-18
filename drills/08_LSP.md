# 第8章ドリル：LSP

← [目次へ戻る](../index.md)　｜　参照: [`nvim_engineer_reference.md` §8](../nvim_engineer_reference.md)

---

## 準備

LSP を使うには Python の言語サーバーが必要です。未設定の場合は先に設定してください：

1. `:Mason` を開いてください
2. `pyright` または `basedpyright` を検索してインストールしてください
3. `:LspInfo` でサーバーが起動していることを確認してください

```
nvim practice/08_LSP_practice.py
```

---

## 練習問題

### Q1. `K` でホバードキュメントを表示する

1. `calculate_area` という関数呼び出しの上にカーソルを置いてください
2. `K` を押してください（型・シグネチャ・docstring が浮かびウィンドウで表示される）
3. もう一度 `K` を押すとウィンドウ内に入れます。`q` で閉じてください

> **目標**: 関数の引数や型を確認するためにマウスでホバーするのをやめて `K` を使う。

---

### Q2. `gd` で定義へジャンプする（最頻出）

1. `calculate_area(width, height)` の呼び出し行で `calculate_area` の上にカーソルを置いてください
2. `gd` を押してください（関数の定義行にジャンプする）
3. `Ctrl-o` を押してください（ジャンプ前の位置に戻る）

> **目標**: 関数の実装を確認したいとき、スクロールせず `gd` → 確認 → `Ctrl-o` で戻る。

---

### Q3. `gr` で参照一覧を表示する

1. `UserProfile` クラスの定義行にカーソルを置いてください
2. `gr` を押してください（このシンボルが使われている箇所の一覧が Telescope で開く）
3. 一覧から任意の箇所に移動してください
4. `Ctrl-o` で戻ってください

---

### Q4. `<leader>rn` でシンボルをリネームする

1. `old_variable` という変数名の上にカーソルを置いてください
2. `<leader>rn` を押してください
3. 新しい名前 `new_variable` を入力して `Enter` を押してください
4. ファイル内の `old_variable` がすべて `new_variable` に変更されたことを確認してください
5. `u` でアンドゥしてください

> **目標**: 変数・関数のリネームには検索置換ではなく `<leader>rn` を使う（LSP が参照を追跡するため安全）。

---

### Q5. `<leader>ca` でコードアクションを実行する

1. `import` が足りない箇所（エラーが表示されている行）にカーソルを置いてください
2. `<leader>ca` を押してください
3. 利用可能なアクション一覧が表示されます（例: "Add import"）
4. 適切なアクションを選択してください

> **ヒント**: エラーが赤く表示されている行で `<leader>ca` を押すと自動修正の選択肢が出ることがあります。

---

### Q6. 診断（エラー・警告）を移動する

1. `]d` を押してください（次の診断へジャンプ）
2. `<leader>e` を押してください（カーソル位置の診断を詳細表示）
3. `[d` を押してください（前の診断へ戻る）
4. `]e` を押してください（次のエラーへジャンプ。警告はスキップ）

---

### Q7. `<leader>q` で全診断を quickfix に開く

1. `<leader>q` を押してください
2. quickfix リストにエラー・警告一覧が開きます
3. `:cn` で次の診断へ、`:cp` で前の診断へ移動してください
4. `:cclose` で quickfix を閉じてください

---

### Q8. 総合チャレンジ

1. `calculate_volume` の呼び出し箇所にカーソルを置き、`gd` で定義に飛び、`K` でドキュメントを確認し、`Ctrl-o` で戻ってください
2. `temp_value` という変数を `<leader>rn` で `computed_result` にリネームしてください
3. `]e` でエラーを巡回して `<leader>e` で内容を確認してください

---

## 練習用ファイル

`practice/08_LSP_practice.py` を作成してください：

```python
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
```
