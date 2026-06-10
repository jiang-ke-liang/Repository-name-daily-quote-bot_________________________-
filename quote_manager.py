import random
import datetime
import json


class Quote:
    """名言类"""
    def __init__(self, content, author, category):
        self.content = content
        self.author = author
        self.category = category
    
    def __str__(self):
        return f"{self.content} —— {self.author}"
    
    def to_dict(self):
        return {
            "content": self.content,
            "author": self.author,
            "category": self.category
        }


class QuoteManager:
    """名言管理器"""
    
    def __init__(self, filename="quotes.json"):
        self.filename = filename
        self.quotes = self._load()
    
    def _load(self):
        """加载数据"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Quote(d["content"], d["author"], d["category"]) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save(self):
        """保存到文件"""
        data = [q.to_dict() for q in self.quotes]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def add(self, content, author, category):
        """添加名言"""
        if not content or not content.strip():
            print("❌ 名言内容不能为空！")
            return False
        if not author or not author.strip():
            print("❌ 作者不能为空！")
            return False
        if not category or not category.strip():
            print("❌ 分类不能为空！")
            return False
        
        new_quote = Quote(content, author, category)
        self.quotes.append(new_quote)
        self.save()
        print("✅ 添加成功！")
        return True
    
    def delete(self, index):
        """删除名言"""
        if not self.quotes:
            print("❌ 暂无名言可删除")
            return False
        if 1 <= index <= len(self.quotes):
            deleted = self.quotes.pop(index - 1)
            self.save()
            print(f"✅ 已删除：{deleted}")
            return True
        else:
            print(f"❌ 编号无效，请输入 1-{len(self.quotes)}")
            return False
    
    def update(self, index, content=None, author=None, category=None):
        """修改名言"""
        if not self.quotes:
            print("❌ 暂无名言可修改")
            return False
        if 1 <= index <= len(self.quotes):
            quote = self.quotes[index - 1]
            if content:
                quote.content = content
            if author:
                quote.author = author
            if category:
                quote.category = category
            self.save()
            print(f"✅ 已修改：{quote}")
            return True
        else:
            print("❌ 编号无效")
            return False
    
    def get_daily(self):
        """今日名言"""
        if not self.quotes:
            return None
        today = datetime.date.today()
        random.seed(today.toordinal())
        return random.choice(self.quotes)
    
    def get_by_category(self, category):
        """按分类筛选"""
        return [q for q in self.quotes if q.category == category]
    
    def get_all(self):
        """获取全部"""
        return self.quotes