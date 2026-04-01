class TrieNode{
    child:{[key:string]:TrieNode}
    isEnd:boolean
    constructor() {
        this.child={}
        this.isEnd = false
    }
}
class Trie {
    root:TrieNode
    constructor() {
    this.root =new TrieNode
    }

    insert(word: string): void {
        let curr = this.root
        for(let i of word){
            if(!curr.child[i]){
                curr.child[i] = new TrieNode
            }
            curr = curr.child[i]
        }
        curr.isEnd =true
    }

    search(word: string): boolean {
        let curr=this.root
        for(let i of word){
            if(!curr.child[i]){
                return false
            }
            curr=curr.child[i]

        }
        return curr.isEnd
    }

    startsWith(prefix: string): boolean {
        let curr=this.root
        for(let i of prefix){
            if(!curr.child[i]){
                return false
            }
          curr = curr.child[i]
        }
        return true
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
