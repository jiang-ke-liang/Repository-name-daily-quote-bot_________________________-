import random
import datetime

quotes = [
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "代码未至.bug先行。",
    "程序员三大美德：懒惰、不耐烦、傲慢。 - Larry Wall",
    "Stay hungry, stay foolish. - Steve Jobs",
    "人生苦短,我用Python。"
    "代码是写给人看的，顺便让计算机执行。 - Donald Knuth"
]

def get_daily_quote():
    today = datetime.date.today()
    random.seed(today.toordinal())
    return random.choice(quotes)

if __name__ == "__main__":
    print(f"📅 {datetime.date.today()}")
    print(f"💡 {get_daily_quote()}")