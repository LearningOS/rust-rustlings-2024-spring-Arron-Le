// options3.rs
//
// Execute `rustlings hint options3` or use the `hint` watch subcommand for a
// hint.


struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let y: Option<Point> = Some(Point { x: 100, y: 200 });

    match y {
        Some(p) => println!("Co-ordinates are {},{} ", p.x, p.y),
        _ => panic!("no match!"),
    }
    let _ = y; // Fix without deleting this line.
    //将 y 绑定到一个新的无用的变量。这样做是为了明确告诉编译器我们有意不使用这个变量，并且避免产生未使用变量的警告
}
