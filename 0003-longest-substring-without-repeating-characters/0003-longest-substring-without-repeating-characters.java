class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] arr = new int[50000];
        int len = s.length();
        int count=0; 
        int k = 0;
        for(int i=0; len>i; i++){
            int counter = i;
            for(int j=i+1; len>j; j++){
                String w = s.substring(i, counter+1);
                String o = s.substring(j, j+1);
                //System.out.println(w+"\t"+o+"\t"+count);
                counter++;
                if(w.contains(o)){
                    break;
                }
                else{
                    count++;
                }
            }
            arr[k] = count+1;
            count = 0;
            k++;
        }
        int max = arr[0];
        /*for(int i=0; len>i; i++){
            System.out.println(arr[i]);
        }*/
        for(int i=1; len>i; i++){
            //System.out.println(max);
            if(max<arr[i]){
                max = arr[i];
            }
        }
        return max;
    }
}