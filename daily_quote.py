import random
import datetime
import json


def load_quotes():
    """
    从 quotes.json 文件加载名言数据
    """
    with open("quotes.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_daily_quote():
    """
    获取今日名言（根据日期固定）
    """
    today = datetime.date.today()
    random.seed(today.toordinal())
    quotes = load_quotes()        # ← 列表，用复数 quotes
    return random.choice(quotes)  # ← 从列表里随机选一个


def get_quotes_by_category(category_name):
    """
    根据分类筛选名言
    """
    quotes = load_quotes()        # ← 列表，用复数 quotes
    result = []
    for quote in quotes:          # ← 单个名言，用单数 quote
        if quote["category"] == category_name:
            result.append(quote)
    return result


if __name__ == "__main__":
    print(f"📅 {datetime.date.today()}")
    
    # 今日名言
    quote = get_daily_quote()
    print(f"💡 今日名言：{quote['content']}")
    print(f"   —— {quote['author']} | 分类：{quote['category']}")
    
    # 技术类名言
    print("\n【技术类名言】")
    tech_quotes = get_quotes_by_category("技术")
    for q in tech_quotes:
        print(f"  - {q['content']}（{q['author']}）")
    
    # 测试类名言
    print("\n【测试类名言】")
    test_quotes = get_quotes_by_category("测试")
    for q in test_quotes:
        print(f"  - {q['content']}（{q['author']}）")