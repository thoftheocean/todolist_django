# coding: utf-8
# author: spareribs
from django import template
import datetime

register = template.Library()

@register.filter()
def time_before(d):
    # 如果不是datetime类型转换后与datetime比较
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day, d.hour, d.minute, d.second)
    now = datetime.datetime.now()
    # d = d.strftime("%Y-%m-%d %H:%M:%S") #这种操作会将datetime.datetime对象转化为字符串对象
    # now = now.strftime("%Y-%m-%d %H:%M:%S")#这种操作会将datetime.datetime对象转化为字符串对象

    d = datetime.datetime(d.year, d.month, d.day, d.hour, d.minute, d.second)
    now = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

    print('创建时间', d, type(d))
    print('当前时间', now, type(now))
    delta = (now-d)
    print(delta)
    # 忽略毫秒
    before = delta.days * 24 * 60 * 60 + delta.seconds
    print('过去了多少秒', before)
    # 刚刚过去的1分钟
    chunks = (
        (60 * 60 * 24 * 365, u'年'),
        (60 * 60 * 24 * 30, u'月'),
        (60 * 60 * 24 * 7, u'周'),
        (60 * 60 * 24, u'天'),
        (60 * 60, u'小时'),
        (60, u'分钟'),
        (1, u'秒'),
    )

    if before < 60:
        return u'刚刚'
    for seconds, unit in chunks:
        # print(seconds, unit)
        count = before // seconds
        if count != 0:
            break
    return str(count) + unit + u"前发布"