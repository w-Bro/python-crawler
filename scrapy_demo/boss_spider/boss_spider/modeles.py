from datetime import datetime, timedelta


class ProxyModel(object):
    def __init__(self, data):
        self.ip = data['ip']
        self.port = data['port']
        self.expire_str = data['expire_time']
        self.blacked = False

        # yyyy-mm-dd hh:mm:ss
        date_str, time_str = self.expire_str.split(' ')
        year, month, day = date_str.split('-')
        hour, minute, second = time_str.split(':')
        self.expire_time = datetime(year=int(year), month=int(month), day=int(day),
                                    hour=int(hour), minute=int(minute), second=int(second))

        # https://ip:port
        self.proxy = 'https://{}:{}'.format(self.ip, self.port)

    #  判断ip是否即将过期
    # 将函数变为属性,直接调用，不用加括号
    @property
    def is_expiring(self):
        now = datetime.now()
        # 小于5秒
        if (self.expire_time - now) < timedelta(seconds=5):
            return True
        else:
            return False
