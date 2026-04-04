// 1. String concatenation
console.log("my" + " cat");
console.log('1' + 2);
console.log(`string literals ' 1+2 = ${1 + 2}`);

// 2. Numeric operators
console.log(1 + 1);  // add
console.log(1 - 1);  // substract
console.log(1 / 1);  // divide
console.log(1 * 1);  // multiply
console.log(5 % 2);  // remainder
console.log(2 ** 3); // exponentiation

// 3. Increment and decrement operators
let counter = 2;
const preIncrement = ++counter;
// counter = counter +1;
// preIncrement = counter;
console.log(`preIncrement : ${preIncrement}, counter: ${counter}`)
const postIncrement = counter++;
// postIncrement = counter;
// counter = counter+1;


// 4. Assignment operators
let x = 3;
let y = 6;

x += y;  // x = x + y;
x -= y;  // x = x - y;
x *= y;  // x = x * y;
x /= y;  // x = x / y;


// 5. Comparison operators
console.log(10 > 6);   // less than
console.log(10 <= 6);  // less than or equal
console.log(10 > 6);   // greater than
console.log(10 >= 6);  // greater than or equal

//6. logical operators : || (or), && (and), ! (not)
const value1 = false;
const value2 = 4 < 2;

// || (or)
console.log(`or: ${value1 || value2 || check()}`);

function check() {
    for (let i = 0; i < 10; i++) {
        // wasting time
        console.log('Ω');
    }
    return true;
}

// && (or)
console.log(`or: ${value1 && value2 && check()}`);

function check() {
    for (let i = 0; i < 10; i++) {
        // wasting time
        console.log('Ω');
    }
    return true;
}

// 7. Equality
const stringFive = '5';
const numberFive = 5;

// == loose equlity, with type conversion
console.log(stringFive == numberFive);
console.log(stringFive != numberFive);

// === Strice equality, no type conversion
console.log(stringFive === numberFive);
console.log(stringFive !== numberFive);

// object equality by reference
const ellie1 = { name: 'ellie' };
const ellie2 = { name: 'ellie' };
const ellie3 = ellie1;
console.log(ellie1 == ellie2);
console.log(ellie1 === ellie2);
console.log(ellie1 === ellie3);


// equality - pzzler
// ==는 블리언을 비교하는 것이고, ===는 값을 비교하는 것이다.
console.log(0 == false);   // T
console.log(0 === false);  // F
console.log('' == false);  // T
console.log('' === false); // F
console.log(null == undefined);  // T 
console.log(null === undefined); // F


// 8. Conditional operators : if
// if, else if, else
name = "ellie";
if (name === 'ellie') {
    console.log("Welcome, Ellie!");
} else if (name === 'coder') {
    console.log('You are amazing coder');
} else {
    console.log('unkwnon')
}


// 9. Ternary operator : ?
// condition ? value1 : value2;
console.log(name === 'ellie' ? 'yes' : 'no');

// 10. Switch statement
// use for multiple if checks
// use for enum-like value check
// use for multiple type checks in TS
const browser = 'IE';
switch (browser) {
    case 'IE':
        console.log('go away!');
        break;
    case 'Chrome':
        console.log('love you!');
        break;
    case 'Firefox':
        console.log('love you!');
        break;
    default:
        console.log('same all!');
        break
}

// 11. loops
// while loop, while the condition is truthy,
// body code is executed.
let i = 3;
while (i > 0) {
    console.log(`while: ${i}`);
    i--;
}

// do while loop, body code is executed first,
// then check the condition.
do {
    console.log(`do while: ${i}`);
    i--;
} while (i > 0);

// for loop, for(beginl conditionl step)
for (i = 3; i > 0; i--) {
    console.log(`for: ${i}`);
}

for (let i = 3; i > 0; i = i - 2) {
    // inline varialbe declaration
    console.log(`inline variable for : ${i}`);
}

// nested loops
for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
        console.log(`i: ${i}, j: ${j}`);
    }
}

// break, continue
for (let i = 0; i < 11; i++) {
    if (i % 2 !== 0) {
        continue;
    }
    console.log(`q1. ${i}`);
}

for (let i = 0; i < 11; i++) {
    if (i > 8) {
        break;
    }
    console.log(`q1. ${i}`);
}

// 12. 배열의
a = [1, 2, 3, 4, 5];
console.log(a);
console.log(a[3]);  // Javascript는 배열을 0부터 index를 시삭한다.
console.log(a.length);

// 배열의 조작
a.push("하하하");    // push는 데이터를 맨 뒤에서 밀어 넣는다.
console.log(a);
a[0] = 111;
a[1] = 222;
console.log(a);

let movies = ['극한직업', '어벤저스', '오펀', '강시', '나홀로 집에', '내부자들']

for (i = 0; i < movies.length; i++) {
    console.log(movies[i]);
}

// 13. 함수
function 인사(이름) {
    console.log('안녕? 나는 ' + 이름 + '야.');
}
인사('일분이');

function 더하기(a, b) {   // a, b 는 매개변수(parameter)
    return a + b;
}
console.log(더하기(100, 200));

document.write(더하기(100, 200));  // web에 써준다

// 14. Object

let person = {};
person.name = "동네79";
person.age = 12;
person.introduce = function () {   // 특성중 값이 함수도 할 수도 있다
    console.log('안녕? 나는 ' + person.name + '야. 나이는 ' + person.age + '살이야')
}

person.introduce();

let person2 = {
    name: "Zena",
    age: 20,
    introduce: function () {
        console.log('안녕 나는 ' + person2.name + '야. 나이는 ' + person2.age + '살이야.');
    }
};

person2.introduce();

function person3(username, age) {
    this.username = username;
    this.age = age;
    this.introduce = function () {
        console.log('안녕? 나는 ' + this.username + "이야. 나이는 " + this.age + '살이야');
    }
}

let p1 = new person3('동네79', 20)
let p2 = new person3('일분이', 3)


p1.introduce();
p2.introduce();

// 생성자(constructor)
function Person4(username, age) {
    this.username = username;
    this.age = age;
    this.introduce = function () {
        console.log('안녕? 나는' + this.username + '야, 나이는 ' + this.age + '살이야.')
    }
}

// 인스턴스(instance)
// new를 넣어야만 this가 윈도우객체를 사용하지 않는다. 반드시 new를 써준다.
let p3 = new Person4('동네79', 20);
let p4 = new Person4('일분이', 3);

p3.introduce();
p4.introduce();


