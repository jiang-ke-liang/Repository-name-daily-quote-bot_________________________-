import random
import datetime
import json


def load_quotes():
    """加载名言"""
    try:
        with open("quotes.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_quotes(quotes):
    """保存名言到文件"""
    with open("quotes.json", "w", encoding="utf-8") as file:
        json.dump(quotes, file, ensure_ascii=False, indent=2)


def get_daily_quote():
    """获取今日名言"""
    today = datetime.date.today()
    random.seed(today.toordinal())
    quotes = load_quotes()
    if not quotes:
        return None
    return random.choice(quotes)


def get_quotes_by_category(category_name):
    """按分类筛选"""
    quotes = load_quotes()
    result = []
    for quote in quotes:
        if quote["category"] == category_name:
            result.append(quote)
    return result


def add_quote(content, author, category):
    """添加新名言"""
    quotes = load_quotes()
    new_quote = {
        "content": content,
        "author": author,
        "category": category
    }
    quotes.append(new_quote)
    save_quotes(quotes)
    print("✅ 名言添加成功！")