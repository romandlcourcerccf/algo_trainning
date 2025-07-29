mpl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut l:usize = 0;
        let mut r:usize = (numbers.len()-1).try_into().unwrap();

        let mut res: Vec<i32> = Vec::new();

        while l <= r {

            if numbers[l] + numbers[r] == target {

                res.push((l+1) as i32);
                res.push((r+1) as i32);
                
                break;

            } else if numbers[l] + numbers[r] < target {
                l +=1;
            } else {
                r -=1;
            }
        }

        return res
    }
}