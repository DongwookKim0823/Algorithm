class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        
        for (int x = 0; x < r2 + 1; x++) {
            int maxY = (int)Math.floor(Math.sqrt(Math.pow(r2, 2) - Math.pow(x, 2)));
            int minY;
            if (x < r1) {
                minY = (int)Math.ceil(Math.sqrt(Math.pow(r1, 2) - Math.pow(x, 2)));
            } else {
                minY = 0;
            }
            
            answer += (maxY - minY + 1);
        }
        
        return (answer - (r2 - r1 + 1)) * 4;
    }
}
