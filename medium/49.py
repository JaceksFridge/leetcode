

strs = ["eat","tea","tan","ate","nat","bat"]

class Solution(object):
    def groupAnagrams(self, strs):


        prevHash = {} # sorted(str) : list of unsorted str
        
        for st in strs:
            sorted_st = "".join(sorted(st))
            if sorted_st in prevHash:
                prevHash[sorted_st].append(st)
            else:
                prevHash[sorted_st] = [st]
            
            
        master_list = list(prevHash.values())
        return master_list


# hashmap | 

# loop strs


    # is sorted str = in hashmap
        # add str to sorted(str) key
    # else
        # make sorted key and assign array value

# loop over hash and add values to masterlist
    
    
    
    
    
s = Solution()
s.groupAnagrams(strs)