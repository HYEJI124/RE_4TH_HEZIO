# Utilities.py - 유용한 기능 모음

def format_phone(number):
    """전화번호 포맷팅"""
    # 01012345678 → 010-1234-5678
    if len(number) == 11:
        return f"{number[:3]}-{number[3:7]}-{number[7:]}"
    return number

def is_valid_email(email):
    """이메일 유효성 검사"""
    return '@' in email and '.' in email

def calculate_age(birth_year):
    """나이 계산"""
    import datetime
    current_year = datetime.datetime.now().year
    return current_year - birth_year

class Timer:
    """시간 측정 클래스"""
    def __init__(self):
        import time
        self.start_time = time.time()
    
    def elapsed(self):
        import time
        return time.time() - self.start_time

# 상수 정의
MAX_RETRY = 3
DEFAULT_TIMEOUT = 30
API_KEY = "your-api-key-here"