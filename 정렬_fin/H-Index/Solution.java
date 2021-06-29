class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int count;
        int not_count;
        boolean tf = false;
        while(true) {
            count=0;
            not_count=0;
            for(int i = 0;i < citations.length;i++) {
                if(answer <= citations[i])
                    count++;
                else
                    not_count++;
            }
            if(count>=answer&& not_count<=answer) {
                tf = true;
            }
            else{
                if(tf == true)
                    break;
            }
            answer++;
        }
        answer--;
        return answer;
    }
}