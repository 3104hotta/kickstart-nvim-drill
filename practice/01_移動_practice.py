# 練習用ファイル: 01_移動_practice.py
# このファイルを nvim で開いて移動コマンドを練習してください


def calculate_total(prices: list[float]) -> float:
    """商品の合計金額を計算する。"""
    result = sum(price for price in prices)
    return result


def apply_discount(price: float, discount: float) -> float:
    """割引率を適用した価格を返す。"""
    if discount < 0 or discount > 1:
        raise ValueError("割引率は0以上1以下である必要があります")
    result = sum(price * (1 - discount) for price in [price])
    return result


def format_price(amount: float, currency: str = "JPY") -> str:
    """金額を通貨記号付きの文字列にフォーマットする。"""
    if currency == "JPY":
        return f"¥{amount:,.0f}"
    elif currency == "USD":
        return f"${amount:,.2f}"
    else:
        raise ValueError(f"未対応の通貨: {currency}")


def generate_receipt(items: list[dict], discount: float = 0.0) -> str:
    """領収書の文字列を生成する。"""
    lines = []
    for item in items:
        name = item["name"]
        price = item["price"]
        discounted = apply_discount(price, discount)
        lines.append(f"  {name}: {format_price(discounted)}")
    total = calculate_total([apply_discount(i["price"], discount) for i in items])
    lines.append(f"合計: {format_price(total)}")
    return "\n".join(lines)


# エントリーポイント
if __name__ == "__main__":
    items = [
        {"name": "りんご", "price": 150.0},
        {"name": "バナナ", "price": 80.0},
        {"name": "みかん", "price": 120.0},
    ]
    receipt = generate_receipt(items, discount=0.1)
    print(receipt)
