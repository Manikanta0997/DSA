class Solution {
    public int maxArea(int[] height) {
        int n = height.length;
        int max = 0;
        int area;
        for(int i=0; n>i; i++){
            for(int j=n-1; j>=1; j--){
                if(height[j] >= height[i]){
                    area = height[i] * (j-i);
                    if(max < area){
                        max = area;
                    }
                    break;
                }
                else{
                    area = height[j] * (j-i);
                    if(max < area){
                        max = area;
                    }
                }
            }
        }
        return max;
    }
}