import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int cnt = 0;
        
        Arrays.sort(citations);
        
        int length = citations.length;
        for(int i = 0; i<length;i++){
            if(citations[length - i -1] <= cnt) break;
            cnt++;
        }
        return cnt;
    }
}
