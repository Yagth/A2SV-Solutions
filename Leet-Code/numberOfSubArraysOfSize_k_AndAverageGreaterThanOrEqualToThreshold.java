class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int i = 0;
        int j = i + k - 1;
        int sum = 0;
        int num = 0;
        
        for(int l = 0; l <= j; l++){
            sum += arr[l];
        }
                
        while(j < arr.length){
            int avg = sum / k;
            if(avg >= threshold) num++;
            
            sum -= arr[i];
            
            if(j+1 < arr.length) sum += arr[j+1]; 
            
            i++;
            j++;
        }
        
        return num;
    }
}
