from abc import ABC, abstractmethod

class Formatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass 

class PlainFormatter(Formatter):
    def format(self, message: str) -> str:
        # Return the message as-is
        return message

class JsonFormatter(Formatter):
    def format(self, message: str) -> str:
        # Return the message wrapped in JSON: {"log": "message"}
        return f"{{\"log\": \"{message}\"}}"
    

class Logger:
    def __init__(self, formatter: Formatter):
        self._formatter = formatter

    def log(self, message: str) -> None:
        # Use the formatter to format the message, then print the result
        print(self._formatter.format(message))
    
if __name__ == "__main__":
    plain_logger = Logger(PlainFormatter())
    plain_logger.log("Server started on port 8080")

    json_logger = Logger(JsonFormatter())
    json_logger.log("Server started on port 8080") 