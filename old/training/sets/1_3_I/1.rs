// source ~/.bash_profile 

use std::fs::read_to_string;
use std::collections::HashSet;

fn read_lines(f_name: &str) -> Vec<String> {
    read_to_string(f_name)
    .unwrap()
    .lines()
    .map(String::from)
    .collect()
}
fn main() {
    let lines = read_lines("input.txt");

    let mut s_1: HashSet<String> = HashSet::new();
    let mut res_1: HashSet<String> = HashSet::new();
    // let  mut gines_counter:  HashMap<String, usize> = HashMap::new();
    
    for i in 0..lines[1].chars().count()-1 {
        let slice = &lines[1][i..i+2];
        //  println!(">>{}", slice);
        s_1.insert(slice.to_string());
    }

    let mut counter = 0;
    for i in 0..lines[0].chars().count()-1 {
        let slice = &lines[0][i..i+2];
        if s_1.contains(&slice.to_string()) {
            // println!("{}", slice);
            res_1.insert(slice.to_string());
            counter = counter + 1;
            // gines_counter.entry(slice.to_string()).or_insert(1);
        }
    }

    println!("{}", counter)

}


