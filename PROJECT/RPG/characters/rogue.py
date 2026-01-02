import random
from characters.character import Character

# 도적 클래스
class Rogue(Character): # Character 상속
    def __init__(self, name='도적'):
        super().__init__(name=name, health=90, attack_power=12)

    # 기본 공격
    def attack(self, target):
        print(f'{self.name}님의 기본 공격!')
        print()
        target.take_damage(self.attack_power)

    # 특수 공격: 급습 (70% 확률로 3배 피해)
    def special_attack(self, target):
        print(f'{self.name}님의 특수 공격!')
        print('[급습]')
        print()
        if random.random() <= 0.7:
            damage = self.attack_power * 3
            target.take_damage(damage)
            print(f'{self.name}님 70% 확률로 특수 공격 성공!')
        else:
            print(f'{self.name}님 특수 공격 실패!')
