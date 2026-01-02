from abc import ABC, abstractmethod

# 1. 추상 클래스 Character 생성
# 모든 캐릭터의 공통 속성과 메서드를 정의
class Character(ABC):
    def __init__(self, name='캐릭터', level=1, health=100, attack_power=10, mana=50):
        self.name = name
        self.level = level
        self.max_health = health  # 최대 체력
        self.health = health      # 현재 체력
        self.attack_power = attack_power
        self.mana = mana          # 현재 마나
        self.max_mana = mana      # 최대 마나
        print()
        print(f'캐릭터 생성: {name} / LV. {level} / HP. {health} / ATK: {attack_power} / MP: {mana}')
        print()

    # 기본 공격 메서드 (서브클래스에서 반드시 구현)
    @abstractmethod
    def attack(self, target):
        pass

    # 특수 공격 메서드 (서브클래스에서 반드시 구현)
    @abstractmethod
    def special_attack(self, target):
        pass

    # 피해를 입는 메서드
    def take_damage(self, damage):
        damage = max(0, damage)  # 음수 피해 방지, 최소 체력 = 0
        self.health -= damage # damage 당한 만큼 HP 감소
        print(f'{self.name}님이(가) {damage}만큼 피해를 입었습니다!')
        print(f'남은 HP: {self.health}')
        print()
        if self.health <= 0: # HP가 0보다 작으면 쓰러짐
            print(f'{self.name}님이 쓰러졌습니다.')

    # 캐릭터 생존 여부 확인
    def is_alive(self):
        return self.health > 0

    # 현재 상태 출력
    def show_status(self):
        print(f'현재 {self.name}님의 상태')
        print(f'LV.{self.level} | HP: {self.health}/{self.max_health} | ATK: {self.attack_power} | 마나: {self.mana}/{self.max_mana}')

    # 체력 회복
    def reset_health(self):
        self.health = self.max_health # 초기 체력이 최대 체력
        print(f'{self.name}님의 체력이 회복되었습니다.')
        print(f'HP: {self.health})')

    # 마나 회복
    def reset_mana(self):
        self.mana = self.max_mana # 초기 마나가 최대 마나
        print(f'{self.name}님의 마나가 회복되었습니다.')
        print(f'마나: {self.mana})')

    # 이름 접근
    def get_name(self):
        return self.name