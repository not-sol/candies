from entities.hello_entity import HelloEntity


class HelloService:
    def get_hello(self) -> HelloEntity:
        return HelloEntity(message="Hello World")
