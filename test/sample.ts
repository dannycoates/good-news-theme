// Type annotations
interface User {
  id: number;
  name: string;
  email?: string;
  readonly createdAt: Date;
}

type Status = "pending" | "active" | "inactive";
type Callback<T> = (data: T) => void;

// Generics
function identity<T>(arg: T): T {
  return arg;
}

class Container<T> {
  private value: T;

  constructor(value: T) {
    this.value = value;
  }

  getValue(): T {
    return this.value;
  }
}

// Decorators
function logged(target: any, key: string, descriptor: PropertyDescriptor) {
  const original = descriptor.value;
  descriptor.value = function(...args: any[]) {
    console.log(`Calling ${key}`);
    return original.apply(this, args);
  };
}

class Service {
  @logged
  process(data: string): boolean {
    return data.length > 0;
  }
}

// Enums
enum Direction {
  Up = 1,
  Down,
  Left,
  Right,
}

// Type guards
function isString(value: unknown): value is string {
  return typeof value === "string";
}

// Utility types
type Partial<T> = { [P in keyof T]?: T[P] };
type Required<T> = { [P in keyof T]-?: T[P] };
