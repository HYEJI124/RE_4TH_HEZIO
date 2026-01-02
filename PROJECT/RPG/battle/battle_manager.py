import random
import time

# 전투 매니저: 턴 기반 전투 진행
class BattleManager:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print('='*50)
        print(' '*20, '전투 시작!', ' '*20)
        print('='*50)
        self.player.show_status() # 사용자의 현재 상태를 보여줌
        print()
        self.enemy.show_status() # 상대방의 현재 상태를 보여줌

        time.sleep(1.5)

        turn = random.choice([self.player, self.enemy])  # 첫 공격자 랜덤
        print(f'첫 번째 공격자: {turn.name}\n')

        player_turn_count = 0 # 사용자의 공격 횟수 셈
        enemy_turn_count = 0 # 상대방의 공격 횟수 셈

        while self.player.is_alive() and self.enemy.is_alive(): # 사용자와 상대방 모두 살아있는 동안 실행됨
            attacker = turn # 공격자 턴
            defender = self.enemy if attacker == self.player else self.player # 공격자가 사용자면 방어자는 상대방

            if attacker == self.player: # 공격자가 사용자일 경우
                player_turn_count += 1 # 사용자의 공격 횟수 증가
                print(f'==== {self.player.name}님의 {player_turn_count}번째 공격 ====')
                print()
            else: # 상대방이 적일 경우
                enemy_turn_count += 1 # 상대방의 공격 횟수 증가
                print(f'==== {self.enemy.name}님의 {enemy_turn_count}번째 공격 ====')
                print()

            try: # 공격자가 방어자에게 공격
                # 70% 확률로 기본 공격, 30% 확률로 특수 공격
                if random.random() <= 0.7:
                    attacker.attack(defender)
                else:
                    attacker.special_attack(defender)
            except Exception as e:
                print(f'{e} -> 기본 공격 진행')
                attacker.attack(defender)

            time.sleep(3)
            print()

            # 다음 턴: 방어자가 생존하면 방어자가 공격하는 턴
            if defender.is_alive():
                turn = defender
            else:
                break

        # 전투 결과 출력
        if self.player.is_alive(): # 게임이 끝난 후 사용자가 살아있을 경우
            print(f'{self.player.name}님의 승리!!')
            return True
        else: # 게임이 끝난 후 상대방이 살아있을 경우
            print(f'{self.player.name}님의 패배..')
            return False
