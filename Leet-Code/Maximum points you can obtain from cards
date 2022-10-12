class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int i = 0;
        int j = cardPoints.length - k;
        int sum = 0;
        int maxPoints = 0;
        
        for(int l = j; l<cardPoints.length; l++){
            sum += cardPoints[l];
        }
        
        maxPoints = sum;
        
        System.out.println(sum);
        
        while(j < cardPoints.length){
            sum += (cardPoints[i] - cardPoints[j]);
            maxPoints = Math.max(maxPoints, sum);
            i++;
            j++;
        }
        
        return maxPoints;
             
    }
}
