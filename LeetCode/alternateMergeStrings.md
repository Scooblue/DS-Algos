![merge2stringalternative](https://github.com/user-attachments/assets/62204bf4-973a-4ab6-8b6c-52b24ac90343)


    class Solution(object):
      def mergeAlternately(self, word1, word2):
        
        merger = ""
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)

        
        for i in range(min_len):
            merger += word1[i] + word2[i]

      
        if len1 > len2:
            merger += word1[min_len:]
        else:
            merger += word2[min_len:]

        return merger
          
  
      
