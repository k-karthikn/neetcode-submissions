class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([True for i in details if int(i[11:13]) > 60])
        
    
        