class Solution {
    public int totalFruit(int[] fruits) {
        int lastFruit = -1;
        int secondLastFruit = -1;
        int max = 0;
        int currentMax = 0;
        int lastFruitCount = 0;
        
        for(int fruit : fruits){
            if(fruit == lastFruit || fruit == secondLastFruit){
                currentMax ++;
            } else{
                currentMax = lastFruitCount + 1;
            }
            
            if(fruit == lastFruit){
                lastFruitCount ++;
            } else{
                lastFruitCount = 1;
                secondLastFruit = lastFruit;
                lastFruit = fruit;
            }
            
            max = Math.max(max, currentMax);
        }
        
        return max;
    }
}
