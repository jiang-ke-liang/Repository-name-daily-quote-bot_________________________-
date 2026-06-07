import random
import datetime
import json


def load_quotes():
    """
    从 quotes.json 文件加载名言数据
    """
    try:
        with open("quotes.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ quotes.json 文件未找到")
        print("请确保 quotes.json 文件存在于当前目录，并且格式正确")
        return []
    except json.JSONDecodeError:
        print("❌ quotes.json 文件格式错误")
        print("请检查 quotes.json 文件的格式是否正确")
        return []


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
    print("=" * 40)
    print("📢 每日名言系统")
    print("=" * 40)
    while True:
        print("\n请选择操作: 技术 / 测试 / 人生 / 幽默")
        print("输入 'all' 查看所有名言，输入 'q' 退出")
        user_input = input("请输入你想查看的分类: ").strip()
        if user_input.lower() == 'q':
            print("👋 再见！")
            break
        elif user_input == 'all':
            print("\n【所有名言】")
            all_quotes = load_quotes()
            for q in all_quotes:
                print(f"  - {q['content']}({q['author']}) | 分类：{q['category']}")
        else:
            quotes = get_quotes_by_category(user_input) 
            if quotes:
                print(f"\n【{user_input}类名言】")
                for q in quotes:
                    print(f"  - {q['content']}({q['author']})")
            else:
                print(f"❌ 没有找到分类为 '{user_input}' 的名言，请重新输入。")
    print(f"📅 {datetime.date.today()}")
    
    # 今日名言
    quote = get_daily_quote()
    print(f"💡 今日名言：{quote['content']}")
    print(f"   —— {quote['author']} | 分类：{quote['category']}")
    
    # 技术类名言
    print("\n【技术类名言】")
    tech_quotes = get_quotes_by_category("技术")
    for q in tech_quotes:
        print(f"  - {q['content']}({q['author']})")
    
    # 测试类名言
    print("\n【测试类名言】")
    test_quotes = get_quotes_by_category("测试")
    for q in test_quotes:
        print(f"  - {q['content']}({q['author']})")