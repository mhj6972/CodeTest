import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int max = n - lost.length; // 기본적으로 수업에 참여할 수 있는 학생 수

        Arrays.sort(lost);
        Arrays.sort(reserve);

        for (int i = 0; i < lost.length; i++) {
            for (int j = 0; j < reserve.length; j++) {
                if(lost[i] == reserve[j]) {
                    max++;
                    lost[i] = 0;
                    reserve[j] = 0;
                    break;
                }
            }
        }

        for (int l : lost) {
            if(l == 0) continue;
            for (int i = 0; i < reserve.length; i++) {
                if(reserve[i] == 0) continue;

                int prev = l - 1; // 이전 번호
                int next = l + 1; // 다음 번호

                if (prev == reserve[i] || next == reserve[i]) {
                    max++;
                    reserve[i] = 0;
                    break;
                }
            }
        }
        return max;
    }
}