import java.util.*;
class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        boolean flag = true;
        Integer[] tmp = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(tmp, Comparator.reverseOrder()); // 내림차순
        int i = 0;
        while(flag){
            i++;
            int temp = tmp[0]*i;
            for(int l : tmp){
                if(temp%l!=0) {
                    flag = true;
                    break;
                }
                else flag = false;
            }
        }
        return tmp[0]*i;
    }
}