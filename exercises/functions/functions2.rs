// functions2.rs
//
// Execute `rustlings hint functions2` or use the `hint` watch subcommand for a
// hint.


fn main() {
    call_me(3);
}

fn call_me(num: i32) {///函数定义时要指定参数类型
    for i in 0..num {
        println!("Ring! Call number {}", i + 1);
    }
}
