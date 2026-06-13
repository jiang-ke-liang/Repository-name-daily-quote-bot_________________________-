from quote_manager import QuoteManager


def show_menu():
    print("\n" + "=" * 40)
    print("🎯 每日名言系统")
    print("=" * 40)
    print("1. 查看今日名言")
    print("2. 按分类查看")
    print("3. 添加新名言")
    print("4. 查看全部名言")
    print("5. 删除名言")
    print("6. 更新名言")
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
        
        elif choice == "5":
            quotes = manager.get_all()
            if not quotes:
                print("暂无名言可删除。")
            else:
                print("\n【删除名言】")
                for i, q in enumerate(quotes, 1):
                    print(f"{i}. {q}")
                try:
                    num = int(input("请输入要删除的名言编号："))
                    manager.delete(num)
                except ValueError:
                    print("❌ 请输入有效的数字！")
            
        
        elif choice == "6":
            quotes = manager.get_all()
            if not quotes:
                print("暂无名言可更新。")
            else:
                print("\n【更新名言】")
                for i, q in enumerate(quotes, 1):
                    print(f"{i}. {q}")
                    # 用户输入编号后，可以选择修改内容、作者和分类，留空表示不修改
                # 例如：输入编号后，提示用户输入新的内容、作者和分类，如果用户直接按回车，则保持原值不变    
                try:
                    num = int(input("请输入要更新的名言编号："))
                    content = input("请输入新的名言内容：").strip()
                    author = input("请输入新的作者：").strip()
                    category = input("请输入新的分类：").strip()
                    manager.update(num, content, author, category)
                except ValueError:
                    print("❌ 请输入有效的数字！")
                              
        else:
            print("❌ 无效选择，请重新输入。")


if __name__ == "__main__":
    main()