function kthCharacter(k: number): string {
    let word:string= 'a'
    while (word.length <k){
        let r = word.length
        for(let i =0;i<r;i++){
            word+=String.fromCharCode(word.charCodeAt(i)+1)
        }
    }
    console.log(word)
    return word[k-1]
};
