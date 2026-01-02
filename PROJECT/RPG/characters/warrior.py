from characters.character import Character

# 전사 클래스 (Character 상속)
class Warrior(Character): # Character 상속
    def __init__(self, name='전사'):
        super().__init__(name=name, health=100, attack_power=15)

    # 기본 공격
    def attack(self, target):
        print(f'{self.name}님의 기본 공격!')
        print()
        target.take_damage(self.attack_power)

    # 특수 공격: 강력한 일격, 체력 5 반동 피해
    def special_attack(self, target):
        print(f'{self.name}님의 특수 공격!')
        print('[강력한 일격]')
        print()
        damage = self.attack_power * 2
        target.take_damage(damage)
        self.health = max(0, self.health - 5)  # 반동 피해 적용
        print(f'{self.name}님 특수 공격 사용 반동으로 -5 HP')
        print(f'남은 HP: {self.health})')
