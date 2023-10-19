class BaseModule:
    def __init__(self,operation_id):
        self.id = operation_id
        self.active = False

    ## 鉴权函数
    def authority_check(self,authority):
        if authority & self.id:
            self.active = True

    ## 模块是否启用判断
    def is_activity(self):
        return self.active


if __name__ == "__main__":
    m = BaseModule(4)
    print(m.active)
    m.authority_check(6)
    print(m.active)