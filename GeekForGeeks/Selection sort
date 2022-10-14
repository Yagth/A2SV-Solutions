class Solution
{
	int  select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr[]
        int iMin = i;
        for(int j = i + 1; j<arr.length; j++){
            if(arr[j] < arr[iMin]) iMin = j;
        }
        
        return iMin;   
    	}
	
	void selectionSort(int arr[], int n)
	{
	    //code here
	    for(int i = 0; i<arr.length - 1; i++){
            int iMin = select(arr,i);
            
            int temp = arr[iMin];
            arr[iMin] = arr[i];
            arr[i] = temp;
        }
	}
}
