function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
    asteroids.sort((a,b)=>a-b)
    console.log(asteroids)
    for(let i of asteroids){
        if(mass>=i){
            mass+=i
        }
        else{
            return false
        }
    }
    
    return true
};
