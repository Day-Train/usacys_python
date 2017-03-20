"""

"""


class Host(object):
    def __init__(self, ip):
        self.ip = ip
        self.openports = set()

    def add_port(self, port):
        self.openports.add(port)


