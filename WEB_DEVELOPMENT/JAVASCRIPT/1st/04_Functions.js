// 함수 (Functions)
// 함수는 특정 작업을 수행하는 재사용 가능한 코드 블록
// Python의 def 함수와 유사한 개념

// 함수의 장점
// 1. 코드 재사용: 같은 코드를 반복해서 작성하지 않아도 됨
// 2. 유지보수 용이: 수정이 필요할 때 한 곳만 고치면 됨
// 3. 가독성 향상: 복잡한 로직을 이름으로 표현 가능
// 4. 모듈화: 기능별로 코드를 분리 가능

// 함수 없이 작성 (비효율적)
console.log("안녕하세요, 철수님!");
console.log("안녕하세요, 영희님!");
console.log("안녕하세요, 민수님!");

// 함수 사용 (효율적)
function greet(name) {
  console.log(`안녕하세요, ${name}님!`);
}

greet("철수");
greet("영희");
greet("민수");

// 1. 함수 선언 (Function Declaration)

// 기본 문법:
// function 함수이름(매개변수1, 매개변수2, ...) {
//   // 실행할 코드
//   return 반환값;  // 선택사항
// }

// 호출:
// 함수이름(인수1, 인수2, ...);

console.log();

// 1-1. 매개변수가 없는 함수
function sayHello() {
  console.log("안녕하세요");
}

sayHello(); // "안녕하세요"
sayHello(); // "안녕하세요"

// 1-2. 매개변수가 있는 함수
function greet2(name, age) {
  console.log(`안녕하세요, ${name}님! ${age}세 이시군요`);
}

greet2("철수", 25); // "안녕하세요, 철수님! 25세 이시군요"

// 1-3. 반환값이 있는 함수 (return)
function addNumbers(firstNum, secondNum) {
  return firstNum + secondNum; // 결과를 반환
}

addNumbers(1, 2); // 3을 반환하지만 출력은 안됨

let sumResult = addNumbers(3, 5); // 반환값을 변수에 저장
console.log("sumResult", sumResult); // 8

// 2. 함수 표현식 (Function Expression)
// 함수를 변수에 할당하는 방식

const addWithExpression = function (num1, num2) {
  return num1 + num2;
};

console.log(addWithExpression(1, 2)); // 3

// 3. 화살표 함수 (Arrow Function)
// ES6에서 도입된 더 짧은 문법
// Python의 lambda와 유사

// 3-1. 기본 화살표 함수
const addWithArrow = (num1, num2) => {
  console.log(num1 + num2);
  return num1 + num2;
};

// 3-2. 한 줄일 때 중괄호와 return 생략 가능
const addShort = (num1, num2) => num1 + num2;

// 3-3. 매개변수가 없을 때
const sayHelloArrow = () => console.log("안녕하세요!");
sayHelloArrow(); // "안녕하세요!"

// 3-4. 매개변수가 하나일 때 (괄호 생략 가능)
const doubleNumber = (value) => value * 2;
console.log(doubleNumber(5)); // 10

const doubleWithoutParens = (value) => value * 2; // 괄호 생략 가능
console.log(doubleWithoutParens(7)); // 14

// 3-5. 여러 줄일 때 (중괄호와 return 필요)
const greetPerson = (personName) => {
  let welcomeMessage = `안녕하세요 ${personName}`;
  console.log(welcomeMessage);
  return welcomeMessage;
};

greetPerson("지수"); // "안녕하세요 지수"

// 요약
// 1. 함수 선언: function 이름() { }
// 2. 함수 표현식: const 이름 = function() { }
// 3. 화살표 함수: const 이름 = () => { }
// 4. return: 함수의 결과값을 반환
// 5. 매개변수: 함수에 전달하는 값
// 6. 화살표 함수는 간결하고 현대적인 문법

// 4. 재귀함수 (Recursive Function)
// 재귀함수: 함수가 자기 자신을 호출하는 함수
// 반드시 종료 조건이 필요하며, 그렇지 않으면 무한 루프에 빠짐

const factorial = (n) => {
  // 재귀 함수 종료 조건 (base case)
  if (n == 1) return 1;
  // 재귀 호출: n * (n-1)!
  return n * factorial(n - 1);
};

// 5! = 5 * 4 * 3 * 2 * 1 = 120
factorial(5);
// 실행 과정:
// 5 * factorial(4);
// 5 * 4 * factorial(3);
// 5 * 4 * 3 * factorial(2);
// 5 * 4 * 3 * 2 * factorial(1);
// 5 * 4 * 3 * 2 * 1;

// 5. 스코프 (Scope)
// 스코프: 변수의 유효 범위를 의미
// 전역 스코프(Global Scope)와 지역 스코프(Local Scope)로 구분

// 전역 변수: 어디서든 접근 가능
let globalVar = "전역변수";

function function1() {
  // 지역 변수: 함수 내에서만 접근 가능
  let localVar = "지역변수";
  console.log(globalVar); // 전역 변수 접근 가능
  console.log(localVar); // 지역 변수 접근 가능
}
function1();

console.log(globalVar); // OK
// console.log(localVar);  // Error: localVar는 함수 외부에서 접근 불가

// 6. 콜백 함수 (Callback Function)
// 콜백 함수: 다른 함수의 인자(파라미터)로 전달되는 함수
// 비동기 처리나 이벤트 핸들링에 자주 사용됨

function greet(name, callback) {
  console.log(`안녕하세요 ${name}님!`);
  // 전달받은 콜백 함수 실행
  callback();
}

function sayGoodbye() {
  console.log("안녕히 가세요!");
}

// sayGoodbye 함수를 콜백으로 전달
greet("홍길동", sayGoodbye);
console.log();