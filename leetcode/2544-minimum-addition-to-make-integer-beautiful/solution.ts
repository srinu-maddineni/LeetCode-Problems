function makeIntegerBeautiful(n: number, target: number): number {
    let r = n
    let base = 1
    function digit(n){
        let k =0
        while(n>0){
            k+=n%10
            n = Math.floor(n/10)
        }
        return k
    }
    while (digit(n) > target) {
        let digitVal = Math.floor(n / base) % 10
        let add = (10 - digitVal) % 10

        n += add * base
        base *= 10
    }
    return n - r
};
