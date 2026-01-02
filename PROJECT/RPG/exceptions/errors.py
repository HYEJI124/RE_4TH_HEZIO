# 게임 전용 예외: 마나 부족
class ManaError(Exception):
    def __init__(self, message = '마나가 부족합니다.'):
        super().__init__(message)