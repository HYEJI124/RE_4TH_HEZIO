from characters.character import Character
# characters 폴더에서 character 파일의 Character 클래스 불러옴

# 마법사 클래스
class Mage(Character): # Character 상속
    def __init__(self, name='마법사'): # name 기본값 '마법사'
        super().__init__(name=name, health=80, attack_power=18)

    # 기본 공격
    def attack(self, target):
        print(f'{self.name}님의 기본 공격!')
        print()
        target.take_damage(self.attack_power) # Character 클래스의 함수 사용 -> attack_power만큼 damage 줄 수 있음

    # 특수 공격: 파이어볼, 마나 20 소모
    def special_attack(self, target):
        print(f'{self.name}님의 특수 공격!')
        print('[파이어볼]')
        print()
        if self.mana < 20: # 현재 마나가 20 마나보다 적으면 특수 공격 실행 불가 -> Exception 발생
            raise Exception(f'{self.name}님의 마나가 부족합니다! \n 현재 마나: {self.mana}')
        damage = self.attack_power * 1.5
        target.take_damage(damage)
        self.mana -= 20
        print(f'{self.name}님 20 마나를 사용하여 특수 공격 실행')
        print(f'- 20 마나, 남은 마나: {self.mana}')
