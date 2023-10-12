from abc import ABC,abstractmethod
import xt_module as md
class BaseContainer:
    def __init__(self,authority):
        self.authority = authority


    @abstractmethod
    def register(self,authority):
        """
        在此处对所有模块进行注册
        """
        pass

class XtContainer(BaseContainer):

    def __init__(self,authority):
        super().__init__(authority)
        self.log = md.XtLogModule(1,"test.db")
        self.production = md.XtProductionModule()
        self.register(self.authority)

    def register(self,authority):
        self.log.authority_check(self.authority)

    def generate_log(self, user_name, operation):
        if not self.log.is_activity():
            return False
        self.log.generate_log(user_name,operation)


if __name__ == "__main__":
    c = XtContainer(3)
    print(c.generate_log("jdy","test the container"))