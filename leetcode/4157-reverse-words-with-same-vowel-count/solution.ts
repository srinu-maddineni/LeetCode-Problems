function reverseWords(s: string): string {
    if(s.length ===0){
        return s
    }
    let l = s.split(" ")
    console.log(l)

    let o = 'aeiou'
    function vowelCount(s1:string):number{
        let c =0
    for(let i of s1){
        if(o.includes(i)){
            c++
        }
    }
    return c
    }
    
    let fc = vowelCount(l[0])
    for(let i =1;i<l.length;i++){
        let c = vowelCount(l[i])
        console.log(c,fc)
        if(c === fc ){
           l[i] =  l[i].split("").reverse().join("")
        }
    }
    
    return l.join(" ")
};
