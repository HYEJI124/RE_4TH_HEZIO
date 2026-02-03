// JavaScript 기초

// JavaScript: 웹 페이지에 동적 기능을 추가하는 프로그래밍 언어
// - 1995년 넷스케이프의 브렌던 아이크가 개발
// - 현재는 웹 브라우저뿐만 아니라 서버(Node.js), 모바일 앱 등 다양한 곳에서 사용

// 웹 개발의 3요소
// HTML     구조     버튼 만들기
// CSS      스타일    버튼 꾸미기
// JS       동작     버튼 클릭 시 반응

// 1. 변수 선언 (Variable Declaration)
// 변수: 데이터를 저장하는 공간 (상자와 같은 개념)

// 1-1. let - 재할당 가능한 변수
let name = "홍길동";
console.log(name);

// 재할당: 같은 변수에 새로운 값을 저장
name = "김철수";
console.log(name); // "김철수"

// 1-2. const - 재할당 불가능한 상수 (constant)
const age = 25;
console.log(age); // 25

// age = 30; // ❌ 에러! TypeError: Assignment to constant variable
// console.log(age);

// 1-3. var - 구형 문법 (ES5 이전), 사용 지양
// var는 함수 스코프를 가지며, 호이스팅 등의 문제로 현대에는 사용하지 않음
var oldStyle = "ES5 이전";

// 2. 변수 이름 규칙 (Naming Convention)
const userName = "홍길동"; // camelCase 사용
const userAge = 25;
const isStudent1 = true; // boolean은 is, has 등으로 시작

// * 잘못된 변수명 예시
// const 1name = '홍길동';      // 숫자로 시작 불가
// const user-name = '홍길동';  // 하이픈(-) 사용 불가
// const let = '홍길동';        // 예약어 사용 불가

// 변수 이름 규칙
// - 영문자(a-z, A-Z), 숫자(0-9), 언더스코어(_), 달러($) 사용 가능
// - 숫자로 시작할 수 없음
// - 예약어 사용 불가 (let, const, function 등)
// - camelCase 권장 (첫 단어는 소문자, 이후 단어의 첫 글자는 대문자)

// 3. 데이터 타입 (Data Types)
// JavaScript는 동적 타입 언어: 변수의 타입을 선언할 필요가 없음

// 3-1. 숫자 (Number)
// - 정수와 실수를 구분하지 않음
const studentAge = 25; // 정수
const productPrice = 19.99; // 실수
const temperature = -19; // 음수

console.log(typeof studentAge); // "number"

// 3-2. 문자열 (String)
// - 작은따옴표(''), 큰따옴표(""), 백틱(``) 모두 사용 가능
const personName = "홍길동"; // 큰따옴표
const cityName = "김철수"; // 작은따옴표
const greeting = `이영희`; // 백틱 (템플릿 리터럴)

console.log(typeof greeting); // "string"

// 3-3. 불리언 (Boolean)
// - true 또는 false 두 가지 값만 가짐
const isStudent = true;
const isTeacher = false;

console.log(typeof isStudent); // "boolean"

// 3-4. null과 undefined
// - null: 의도적으로 값이 없음을 나타냄
// - undefined: 값이 할당되지 않은 상태
let emptyValue = null; // 의도적으로 빈값
let undefinedValue; // 값이 할당되지 않음 (자동으로 undefined)

console.log(emptyValue); // null
console.log(undefinedValue); // undefined

// 4. 템플릿 리터럴 (Template Literals)
// Python의 f-string과 유사: print(f'{name} 이고 {age} 이다')

// 기존 방식: 문자열 연결 (+)
console.log("제 이름은 " + name + " 이고, 나이는 " + age + "살 입니다.");

// 템플릿 리터럴: 백틱(`)과 ${} 사용
console.log(`제 이름은 ${name} 이고, 나이는 ${age}살 입니다.`);

// 5. 연산자 (Operators)
// 5-1. 산술 연산자 (Arithmetic Operators)
const firstNumber = 10;
const secondNumber = 3;

console.log(firstNumber + secondNumber); // 13 (덧셈)
console.log(firstNumber - secondNumber); // 7 (뺄셈)
console.log(firstNumber * secondNumber); // 30 (곱셈)
console.log(firstNumber / secondNumber); // 3.333... (나눗셈)
console.log(firstNumber % secondNumber); // 1 (나머지)
console.log(firstNumber ** secondNumber); // 1000 (거듭제곱, 10³)

// 5-2. 증감 연산자 (Increment/Decrement)
let clickCount = 0;
clickCount++; // clickCount = clickCount + 1 (후위 증가)
console.log("clickCount", clickCount); // 1

clickCount--; // clickCount = clickCount - 1 (후위 감소)
console.log("clickCount", clickCount); // 0

// 5-3. 할당 연산자 (Assignment Operators)
let score = 10;
score += 5; // score = score + 5
console.log("score", score); // 15

score -= 3; // score = score - 3
console.log("score", score); // 12

score *= 2; // score = score * 2
console.log("score", score); // 24

// 5-4. 문자열 연산 (String Concatenation)
let firstName = "홍";
let lastName = "길동";

let fullName = firstName + lastName;
console.log("fullName", fullName); // "홍길동"

// 6. 실습 예제 - 변수와 연산자 활용
const myName = "홍길동";
const myAge = 25;
const amIStudent = true;

console.log("이름:", myName);
console.log("나이:", myAge + "살");
console.log("학생:", amIStudent);
console.log(`자기소개: 안녕하세요, 저는 ${myAge}살 ${myName}입니다.`);

// 요약
// 1. 변수 선언: let (재할당 가능), const (재할당 불가)
// 2. 데이터 타입: Number, String, Boolean, null, undefined
// 3. 템플릿 리터럴: `문자열 ${변수}` 형태로 사용
// 4. 연산자: 산술(+, -, *, /, %, **), 증감(++, --), 할당(=, +=, -=, *=)
// 5. typeof 연산자로 데이터 타입 확인 가능
