//! Module documentation
//! This is a crate-level doc comment

use std::collections::HashMap;
use std::io::{self, Read, Write};

/// A user struct with lifetime parameter
#[derive(Debug, Clone, PartialEq)]
pub struct User<'a> {
    pub name: &'a str,
    pub age: u32,
    email: Option<String>,
}

impl<'a> User<'a> {
    /// Creates a new user
    pub fn new(name: &'a str, age: u32) -> Self {
        Self {
            name,
            age,
            email: None,
        }
    }

    pub fn with_email(mut self, email: String) -> Self {
        self.email = Some(email);
        self
    }

    fn is_adult(&self) -> bool {
        self.age >= 18
    }
}

// Traits
pub trait Greeting {
    fn greet(&self) -> String;

    fn greet_formal(&self) -> String {
        format!("Good day, {}", self.greet())
    }
}

impl<'a> Greeting for User<'a> {
    fn greet(&self) -> String {
        format!("Hello, {}!", self.name)
    }
}

// Enums with variants
#[derive(Debug)]
pub enum Status {
    Active,
    Inactive,
    Pending { reason: String },
    Error(String),
}

// Constants
const MAX_USERS: usize = 100;
static GLOBAL_COUNT: std::sync::atomic::AtomicUsize =
    std::sync::atomic::AtomicUsize::new(0);

// Generic function with trait bounds
fn process<T: std::fmt::Debug + Clone>(items: &[T]) -> Vec<T> {
    items.iter().cloned().collect()
}

// Async function
async fn fetch_data(url: &str) -> Result<String, Box<dyn std::error::Error>> {
    // Simulated async operation
    Ok(String::from("data"))
}

fn main() {
    // Variables and mutability
    let x = 5;
    let mut y = 10;
    y += x;

    // Pattern matching
    let status = Status::Active;
    match status {
        Status::Active => println!("Active"),
        Status::Inactive => println!("Inactive"),
        Status::Pending { reason } => println!("Pending: {}", reason),
        Status::Error(e) => eprintln!("Error: {}", e),
    }

    // Closures
    let add = |a: i32, b: i32| -> i32 { a + b };
    let numbers: Vec<i32> = (0..10).filter(|&n| n % 2 == 0).collect();

    // References and borrowing
    let s = String::from("hello");
    let r1 = &s;
    let r2 = &s;
    println!("{} and {}", r1, r2);

    // Macros
    println!("Hello, world!");
    let v = vec![1, 2, 3];
    dbg!(&v);

    // Error handling
    let result: Result<i32, &str> = Ok(42);
    if let Ok(value) = result {
        println!("Value: {}", value);
    }

    // Unsafe block
    unsafe {
        let ptr = &x as *const i32;
        println!("Address: {:?}", ptr);
    }
}

// Macro definition
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
    ($name:expr) => {
        println!("Hello, {}!", $name);
    };
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_user_creation() {
        let user = User::new("Alice", 30);
        assert_eq!(user.name, "Alice");
        assert!(user.is_adult());
    }
}
