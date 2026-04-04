// Whole-script strict mode syntax
'use scrict';


// 2. Variable
// let (ES6에 추간된 문법)

// 블럭 밖에서 선언한 변수는 블럭 안이나 밖에서 모두 사용 가능하다.
let name = 'ellie';
console.log(name);
name = 'hello';
console.log(name);


name = 'Out Block'
{
    // 블럭 안에서 선언한 변수는 블럭 밖에서 사용하지 못한다.
    let name1 = 'In Block';
    name = 'In Block in name';
}
console.log(name);

// name1은 Block 내부에서 선언되었으므로 밖에서 읽지 못한다.
// console.log(name1);


// 3. Contants
// 데이터의 내용을 항상 일정하게 나타낼 경우 사용
// - 보안을 목적으로
// - 실수를 방지할 목적으로

const daysInWeeks = 7;
const maxNumber = 5;


// 4. Variable Types
// primititive : number, string, boolean, null, undefiedn, symbol
// Object : box container  * single items(primititive)를 하나하나 묶어서 관리하는 것
// Function

// Java는 let로 선언해 주면 문자든 숫자든 관계없이 할당해 줄 수 있다.
let a = 12;
let b = 1.2;


const count = 17;  // integer
const size = 17.1; // decimal number
console.log(`value : ${count}, type : ${typeof count}`);
console.log(`value : ${size},type : ${typeof size}`);

//object, ral - life object, data structure
const ellie = { name: 'ellie', age: 20 };
ellie.age = 21;


// 5. Dynamic Typing : Dynamically typed language

let text = 'hello';
console.log(`value: ${text}, type : ${typeof text}`);

text = 1;
console.log(`value: ${text}, type : ${typeof text}`);

text = '7' + 5;  //문자와 숫자를 더할 경우 숫자를 문자로 간주하여 더한다.
console.log(`value: ${text}, type : ${typeof text}`);

text = '10' / '5';  //문자와 문자를 나울때 숫자로 간주하고 나눈다.
console.log(`value: ${text}, type : ${typeof text}`);


