import java.util.*;
import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> list = new ArrayList<>();
        list.add(arr[0]);
        for(int l:arr){
            int temp = l;
            if(list.get(list.size()-1).intValue() != temp) list.add(l);
        }
    
        return list;
    }
}