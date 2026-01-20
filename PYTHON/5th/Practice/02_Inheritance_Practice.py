class Shape:
    def __init__(self, sides, base):
        ''' 변의 개수(sides), 밑변의 길이(base) '''
        self.sides = sides
        self.base = base

    def printinfo(self):
        ''' 변의 개수: 4, 밑변의 길이: 10 '''
        print(f'변의 개수: {self.sides}')
        print(f'밑변의 길이: {self.base}')

    def area(self):
        '''
            메소드를 정의하여 "넓이 계산이 정의되지 않았습니다."라는 메시지를 출력
            -> 자식 클래스에서 이 메소드 오버라이딩 해야 함
        '''
        print(f'넓이 계산이 적용되지 않습니다.')

class Triangle(Shape):
    '''
        생성자에서 sides, base, height를 모두 초기화
        area() 메소드를 오버라이딩하여 (base * height) / 2 값을 출력
    '''

    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height
        print('삼각형 생성')

    def area(self):
        print(f"넓이: {self.base * self.height / 2}")

class Rectangle(Shape):
    '''
        생성자에서 sides, base, height를 모두 초기화
        area() 메소드를 오버라이딩하여 base * height 값을 출력
    '''

    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height
        print('사각형 생성')

    def area(self):
        print(f"넓이: {self.base * self.height}")

rect = Rectangle(4, 10, 5)
tri = Triangle(3, 10, 5)

rect.area()
tri.area()