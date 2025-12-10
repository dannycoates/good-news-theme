// Single-line comment
/* Multi-line
   comment */

/**
 * JSDoc comment
 * @param {string} name - The name parameter
 * @returns {boolean} Returns true if valid
 */
function greetUser(name) {
  const greeting = "Hello";
  let message = `${greeting}, ${name}!`;
  var legacy = 'old style';

  console.log(message);
  return true;
}

// Constants and literals
const MAX_SIZE = 100;
const pi = 3.14159;
const hex = 0xFF;
const binary = 0b1010;
const isActive = true;
const nothing = null;
const missing = undefined;

// Regular expressions
const pattern = /[a-z]+\d*/gi;
const escaped = "line1\nline2\ttabbed";

// Arrow functions
const add = (a, b) => a + b;
const double = x => x * 2;

// Classes and inheritance
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound`);
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }

  speak() {
    console.log(`${this.name} barks!`);
  }
}

// Object literals
const config = {
  host: "localhost",
  port: 3000,
  enabled: true,
  callback: function() {},
  arrow: () => {},
};

// Async/await
async function fetchData(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    throw new Error("Failed to fetch");
  }
}

// Control flow
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    continue;
  }
  while (false) {
    break;
  }
}

// Built-ins
const arr = new Array(5);
const now = Date.now();
const random = Math.random();
const parsed = JSON.parse('{}');
const str = Object.keys({}).toString();
