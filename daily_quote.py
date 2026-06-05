import random
import datetime

# 这个脚本每天显示一句编程相关的名言。通过使用当前日期作为随机数生成器的种子，确保每天显示的名言不同，但在同一天内保持一致。
quotes = [
    {
        "content": "代码未至，bug先行。",
        "author": "佚名",
        "category": "技术"
    },
    {
        "content": "人生苦短，我用Python。",
        "author": "Python社区",
        "category": "技术"
    },
    {
        "content": "Talk is cheap. Show me the code.",
        "author": "Linus Torvalds",
        "category": "技术"
    },
    {
        "content": "Stay hungry, stay foolish.",
        "author": "Steve Jobs",
        "category": "人生"
    },
    {
        "content": "程序员三大美德：懒惰、不耐烦、傲慢。",
        "author": "Larry Wall",
        "category": "幽默"
    }
]



def get_daily_quote():
    # 获取当前日期，并将其转换为一个整数（天数），作为随机数生成器的种子。
    today = datetime.date.today()
    #random.seed()函数用于初始化随机数生成器，使得每次运行程序时生成的随机数序列不同。通过传入一个固定的种子值，可以确保每天生成的随机数序列相同，从而每天显示同一句话。
    random.seed(today.toordinal())
    quote = random.choice(quotes)
    return quote
def get_quote_by_category(category_name):
    """
    根据类别获取名言。
    category_name: 类别名称（如“技术”、“励志”、“幽默”）
    """
    results = []
    # 遍历所有名言，找到匹配类别的名言并添加到结果列表中。
    for quote in quotes:
        if quote["category"] == category_name:
            # 如果名言的类别与输入的类别名称匹配，则将该名言添加到结果列表中。
            results.append(quote)
    return results



if __name__ == "__main__":
    print(f"📅 {datetime.date.today()}")
    #将函数的返回值存储在变量quote中。
    quote = get_daily_quote()
    print(f"  -- {quote['content']} -- {quote['author']} ({quote['category']})")
    print("\n【技术类名言】")
    # 获取技术类名言并打印出来。
    tech_quotes = get_quote_by_category("技术")
    for q in tech_quotes:
        print(f"  -- {q['content']} -- {q['author']}")
 
        





