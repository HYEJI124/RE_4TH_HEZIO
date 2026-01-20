'''
추상 클래스 Payment를 정의하고, pay(amount)를 추상 메소드로 선언(abc 모듈 사용)

CardPayment 클래스와 CashPayment 클래스는 Payment를 상속받아 pay() 메소드를 오버라이딩
    CardPayment: 카드로 {amount}원을 결제합니다.
    CashPayment: 현금으로 {amount}원을 결제합니다.
'''

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f'카드로 {amount}원을 결제합니다.')

class CashPayment(Payment):
    def pay(self, amount):
        print(f'현금으로 {amount}원을 결제합니다.')

card_pay = CardPayment()
card_pay.pay(10000)

cash_pay = CashPayment()
card_pay.pay(2000)