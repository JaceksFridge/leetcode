
words = ["gin","zen","gig","msg"]

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        
        hashmap = {}
        master_arr = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for i in range(len(alpha)):
            hashmap[alpha[i]] = morse[i]

        word_list = ""
        
        for word in words:
            word_list = ""
            for letter in word:
                word_list += hashmap[letter]

            master_arr.append(word_list)
            
        unique = set(master_arr)
        return len(unique)
sol = Solution()
print(sol.uniqueMorseRepresentations(words))
