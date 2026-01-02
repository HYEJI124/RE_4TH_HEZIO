import random
from characters.warrior import Warrior
from characters.mage import Mage
from characters.rogue import Rogue

# 사용자가 캐릭터 이름을 다양하게 입력할 수 있게 해 줌
Character_Choice = {
    '1': Warrior, '전사': Warrior,
    '2': Mage, '마법사': Mage,
    '3': Rogue, '도적': Rogue,
}

# 사용자 캐릭터 선택
def choose_character(prompt_message):
    print(prompt_message)
    while True:
        choice = input('1. 전사 / 2. 마법사 / 3. 도적: ').strip()
        cls = Character_Choice.get(choice)
        if cls:
            name = input('캐릭터 이름 입력 (엔터: 기본 이름): ').strip()
            return cls(name) if name else cls()
        print('잘못된 입력! 1,2,3 또는 전사/마법사/도적 중 선택')

# 랜덤 적 캐릭터 생성
def choose_random_enemy():
    cls = random.choice([Warrior, Mage, Rogue])
    return cls()
