import datetime
from quote_manager import load_quotes, get_daily_quote, get_quotes_by_category, add_quote
from quote_manager import QuoteManager

def show_menu():
    print("\n" + "=" * 40)
    print("🎯 每日名言系统")
    print("=" * 40)
    print("1. 查看今日名言")
    print("2. 按分类查看")
    print("3. 添加新名言")
    print("4. 查看全部名言")
    print("q. 退出")
    print("-" * 40)


def main():
    manager = QuoteManager()
    while True:
        show_menu()
        choice = input("请选择操作：").strip()
        
        if choice == "q":
            print("👋 再见！")
            break
        
        elif choice == "1":
            quote = get_daily_quote()
            if quote:
                print(f"\n📅 {datetime.date.today()}")
                print(f"💡 {quote['content']}")
                print(f"   —— {quote['author']} | 分类：{quote['category']}")
            else:
                print("❌ 暂无名言")
        
        elif choice == "2":
            category = input("请输入分类（技术/人生/幽默/测试）：").strip()
            quotes = get_quotes_by_category(category)
            if not quotes:
                print("该分类下暂无名言。")
            else:
                print(f"\n【{category}类名言】")
                for q in quotes:
                    print(f"  - {q['content']}（{q['author']}）")
        
        elif choice == "3":
            print("\n【添加新名言】")
            content = input("请输入名言内容：").strip()
            author = input("请输入作者：").strip()
            category = input("请输入分类：").strip()
            add_quote(content, author, category)
        
        elif choice == "4":
            print("\n【全部名言】")
            quotes = load_quotes()
            for i, q in enumerate(quotes, 1):
                print(f"{i}. {q['content']}（{q['author']}）[{q['category']}]")
        
        else:
            print("❌ 无效选择，请重新输入。")


if __name__ == "__main__":
    main()