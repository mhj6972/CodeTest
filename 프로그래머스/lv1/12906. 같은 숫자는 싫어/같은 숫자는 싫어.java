import java.util.*;
import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> list = new ArrayList<>();
        list.add(arr[0]);
        for(int l:arr){
            if(list.get(list.size()-1).intValue() != l) list.add(l);
        }
    
        return list;
    }
}