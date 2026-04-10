function recoverOrder(order: number[], friends: number[]): number[] {

    let  res = []
    for(let i of order){
        if(friends.includes(i)){
            res.push(i)
        }
    }
    return  res
};
