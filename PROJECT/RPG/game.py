from utils.helpers import choose_character, choose_random_enemy
from battle.battle_manager import BattleManager

# 게임 루프
def game():
    print('='*50)
    print(' '*17, 'RPG 게임 시작', ' '*17)
    print('='*50)

    player = choose_character("당신의 캐릭터를 선택하세요")
    while True:
        use_random = input('적을 랜덤 생성? (y/n): ').strip().lower()
        print()
        if use_random == 'n':
            enemy = choose_character("상대 캐릭터를 선택하세요")
        else:
            enemy = choose_random_enemy()

        bm = BattleManager(player, enemy)
        won = bm.start_battle()

        if won:
            again = input('새로운 적과 싸우시겠습니까? (y/n): ').strip().lower()
            if again != 'y':
                print('게임 종료!')
                break
            heal = input('전투 후 체력/마나 회복? (y/n): ').strip().lower()
            if heal == 'y':
                player.reset_health()
                player.reset_mana()
        else:
            print('게임 종료!')
            break

if __name__ == '__main__':
    game()
