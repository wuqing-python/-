class A(object):
    def start(self):
        """
        复杂操作
        """
        self.run()

    def run(self):
        pass


class B(A):
    def run(self):
        print("B类设计")


b = B()
b.start()
