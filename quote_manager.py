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


class Quote:
    """名言类"""

    def __init__(self, content, author, category):
        self.content = content
        self.author = author
        self.category = category

    def __str__(self):
        # 返回名言的字符串表示，格式为： "内容" - 作者
        return f'"{self.content}" - {self.author}'
    
    def to_dict(self):
        # 将名言对象转换为字典格式，便于保存到文件
        return {
            "content": self.content,
            "author": self.author,
            "category": self.category
        }
    

class QuoteManager:
    """名言管理器"""

    def __init__(self,filename="quotes.json"):
        self.filename = filename
        self.quotes = self._load()

        
    def _load(self):
        """私有方法：加载数据"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                # 把字典列表转成 Quote 对象列表
                return [Quote(d["content"], d["author"], d["category"]) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save(self):
        """私有方法：保存数据"""
        data = [q.to_dict() for q in self.quotes]
        with open(self.filename, "w", encoding="utf-8") as f:
            # 把 Quote 对象列表转成字典列表
            data = [q.to_dict() for q in self.quotes]
            json.dump(data, f, ensure_ascii=False, indent=2)


    def add(self, content, author, category):
        new_quote = Quote(content, author, category)
        self.quotes.append(new_quote)
        self._save()
        print("✅ 名言添加成功！")


    def get_daily(self):
        """获取今日名言"""
        today = datetime.date.today()
        random.seed(today.toordinal())
        if not self.quotes:
            return None
        return random.choice(self.quotes)
    
    def get_by_category(self, category_name):
        """按分类筛选"""
        return [q for q in self.quotes if q.category == category_name]
    
    def get_all(self):
        """获取所有名言"""
        return self.quotes