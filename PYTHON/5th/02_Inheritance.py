# 상속(Inheritance)
'''
상속:
- 기존 클래스의 속성과 메소드를 물려받아 새로운 클래스를 만드는 것
- "부모의 특징을 자식이 물려받는 것"과 같은 개념

실생활 예시:
- 포유류 → 개, 고양이 (공통: 자기, 먹기)
- 자동차 → 승용차, 트럭 (공통: 운전, 주유)
- 부모 → 자식 (유전자, 성씨 물려받기)

상속을 사용하는 이유
- 코드 중복을 줄임
- 유지보수가 쉬워짐
- 논리적인 계층 구조 표현
'''

# 상속 없으면 코드 중복 많음
print("=== 나쁜 예: 상속 없는 코드 ===")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    def eat(self):
        print(f'{self.name}이(가) 먹습니다.')

    def sleep(self):
        print(f'{self.name}이(가) 잠을 잡니다.')

    def bark(self):  # Dog만의 고유 메소드
        print(f'{self.name}이(가) 멍멍 짖습니다.')


class Cat:
    def __init__(self, name, age):
        self.name = name  # 중복!
        self.age = age    # 중복!

    def eat(self):  # 중복!
        print(f'{self.name}이(가) 먹습니다.')

    def sleep(self):  # 중복!
        print(f'{self.name}이(가) 잠을 잡니다.')

    def meow(self):  # Cat만의 고유 메소드
        print(f'{self.name}이(가) 야옹 웁니다.')


class Bird:
    def __init__(self, name, age):
        self.name = name  # 계속 중복!
        self.age = age    # 계속 중복!

    def eat(self):  # 계속 중복!
        print(f'{self.name}이(가) 먹습니다.')

    def sleep(self):  # 계속 중복!
        print(f'{self.name}이(가) 잠을 잡니다.')

    def fly(self):  # Bird만의 고유 메소드
        print(f'{self.name}이(가) 날아갑니다.')

'''
위 코드의 문제점:
- 너무 많은 중복 -> 수정할 때마다 모든 클래스를 다 고쳐야 함

해결 방법: 상속
'''

# 상속으로 해결
print("\n=== 좋은 예: 상속을 사용한 코드 ===")

# 부모 클래스 (기본 클래스, Base Class)
class Animal:
    """모든 동물의 공통 특징을 가진 부모 클래스 -> 한 번만 정의"""

    def __init__(self, name, age):
        self.name = name
        self.age = age  
        print(f'{name} 동물이 태어났습니다! (나이: {age})')

    def eat(self):
        print(f'{self.name}이(가) 먹습니다.')

    def sleep(self):
        print(f'{self.name}이(가) 잠을 잡니다.')

# 자식 클래스들 (파생 클래스, Derived Class)
class Dog(Animal):  # Animal을 상속받음!
    """개 클래스 - Animal의 모든 기능 + 개만의 기능"""

    def bark(self):  # Dog만의 고유 메소드
        print(f'{self.name}이(가) 멍멍 짖습니다.')

class Cat(Animal):  # Animal을 상속받음!
    """고양이 클래스 - Animal의 모든 기능 + 고양이만의 기능"""

    def meow(self):  # Cat만의 고유 메소드
        print(f'{self.name}이(가) 야옹 웁니다.')

class Bird(Animal):  # Animal을 상속받음!
    """새 클래스 - Animal의 모든 기능 + 새만의 기능"""

    def fly(self):  # Bird만의 고유 메소드
        print(f'{self.name}이(가) 날아갑니다.')

# 사용 예시
print("\n상속받은 클래스 사용하기:")
dog1 = Dog('바둑이', 3)
dog1.eat()    # 부모(Animal)의 메소드 사용
dog1.sleep()  # 부모(Animal)의 메소드 사용
dog1.bark()   # 자식(Dog) 메소드 사용

# 상속 기본 문법과 용어
print("\n=== 상속 기본 문법 ===")

# 기본 문법 구조

class 부모클래스:
    """부모 클래스 (Parent/Base/Super Class)"""
    pass


class 자식클래스(부모클래스):  # 괄호 안에 부모 클래스 이름
    """자식 클래스 (Child/Derived/Sub Class)"""
    pass


'''
상속의 특징:
1. 자식은 부모의 모든 것을 물려받음
2. 부모의 모든 속성과 메서드를 자동으로 사용 가능
3. 자식은 자신만의 속성과 메서드를 추가 가능
4. 부모를 수정하면 모든 자식에 자동 반영
'''

# ==========================================
# 실전 예제: 사람 클래스 상속
# ==========================================
print("\n=== 실전 예제: Person 상속 ===")

class Person:  # 부모 클래스
    """사람의 기본 특징"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'{name}({age}세)가 생성되었습니다.')

    def greet(self):
        print(f'안녕하세요, {self.name}입니다.')


class Student(Person):  # Person을 상속
    """학생 = 사람 + 공부하는 기능"""

    def study(self):
        print(f'{self.name}이(가) 공부합니다.')


class Teacher(Person):  # Person을 상속
    """선생님 = 사람 + 가르치는 기능"""

    def teach(self):
        print(f'{self.name}이(가) 수업합니다.')


# 사용 예시
student = Student('김학생', 20)
teacher = Teacher('박선생', 35)

print("\n부모 클래스의 메소드 호출:")
student.greet()  # Person의 메소드
teacher.greet()  # Person의 메소드

print("\n자식 클래스만의 메소드 호출:")
student.study()  # Student만의 메소드
teacher.teach()  # Teacher만의 메소드

# ==========================================
# super()와 생성자 상속
# ==========================================
print("\n=== super() 사용법 ===")

'''
super()란?
- 자식 클래스에서 부모 클래스에 접근할 때 사용
- "부모님 것을 먼저 처리하고 내 것을 추가"
'''

class Person:
    """부모 클래스"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Person 생성: {name} {age}살')

    def greet(self):
        print(f'안녕하세요. {self.name}입니다.')


class Student(Person):
    """자식 클래스 - super() 사용"""

    def __init__(self, name, age, student_id):
        # 1. 부모의 __init__ 먼저 호출 (이름, 나이 처리)
        super().__init__(name, age)  # 부모 생성자 호출!

        # 2. 자신만의 속성 추가 (학번)
        self.student_id = student_id
        print(f'Student 생성: 학번 {student_id}')

    def greet(self):
        # 부모의 greet() 먼저 호출
        super().greet()
        # 자신만의 내용 추가
        print(f'저는 학생입니다. 학번: {self.student_id}')


# super() 사용 예시
print("\n super() 실행 과정:")
student = Student('김철수', 20, '20250001')
print("\n인사하기:")
student.greet()

# ==========================================
# 메소드 오버라이딩 (Method Overriding)
# ==========================================
print("\n=== 메소드 오버라이딩 ===")

'''
오버라이딩이란?
- 부모 클래스의 메소드를 자식 클래스에서 다시 정의
- "부모님 방식 말고 내 방식대로 하겠다!"
'''

# 기본 동물 소리

class Animal:
    """동물 기본 클래스"""

    def make_sound(self):
        print('동물이 소리를 냅니다.')

# 각 동물마다 다른 소리로 오버라이딩

class Dog(Animal):
    """개 - 멍멍 소리로 오버라이딩"""

    def make_sound(self):  # 부모의 make_sound를 덮어씀!
        print('멍멍!')

class Cat(Animal):
    """고양이 - 야옹 소리로 오버라이딩"""

    def make_sound(self):  # 부모의 make_sound를 덮어씀!
        print('야옹!')

# 오버라이딩 테스트
print("\n 각자 다른 소리 내기:")
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.make_sound()  # 같은 메소드 이름, 다른 동작!


# ==========================================
# 실전 예제: 도형 넓이 계산
# ==========================================
print("\n=== 도형 넓이 계산 (오버라이딩) ===")

class Shape:
    """모든 도형의 부모 클래스"""

    def __init__(self, name):
        self.name = name

    def area(self):
        """넓이 계산 - 자식이 오버라이딩 해야 함"""
        return 0  # 기본값

    def info(self):
        """도형 정보 출력"""
        print(f'{self.name}의 넓이: {self.area():.2f}')

class Rectangle(Shape):
    """직사각형 - 넓이 = 가로 × 세로"""

    def __init__(self, width, height):
        super().__init__('직사각형')  # 부모 생성자 호출
        self.width = width
        self.height = height

    def area(self):  # 오버라이딩!
        return self.width * self.height


class Circle(Shape):
    """원 - 넓이 = π × 반지름²"""

    def __init__(self, radius):
        super().__init__('원')  # 부모 생성자 호출
        self.radius = radius

    def area(self):  # 오버라이딩!
        return 3.14 * self.radius * self.radius


# 도형 넓이 계산
print("\n 각 도형의 넓이:")
shapes = [
    Rectangle(5, 3),  # 5 × 3 = 15
    Circle(4)         # 3.14 × 4 × 4 = 50.24
]

for shape in shapes:
    shape.info()  # 각자 다른 방식으로 넓이 계산!

# ==========================================
# 상속 핵심 정리
# ==========================================
'''
상속(Inheritance) 핵심 정리

상속의 장점
  1. 코드 재사용 - 중복 제거
  2. 유지보수 용이 - 한 곳만 수정
  3. 확장성 - 새 기능 추가 쉬움
  4. 논리적 구조 - 계층 관계 표현

기본 문법
  class 자식클래스(부모클래스):
      # 자식 클래스 내용

super()
  - 부모 클래스 접근
  - 부모 생성자 호출
  - 부모 메소드 호출

오버라이딩
  - 부모 메소드 재정의
  - 자식마다 다른 동작
  - 다형성 구현

요약: 상속은 "물려받고 확장하기"
'''