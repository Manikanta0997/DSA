class Solution {
    public int romanToInt(String s) {
        int len = s.length();
        int sum = 0;
        //int front = 0; back = 0;
        for(int i=0; len>i; i++){
            String e;
            String w = s.substring(i, i+1);
            if(len-1 > i){
                e = s.substring(i, i+2);
                //System.out.println(e);
                if(e.compareTo("IV")==0){
                    sum = sum + 4;
                    i = i + 1;
                }
                else if(e.compareTo("IX")==0){
                    sum = sum + 9;
                    i = i + 1;
                }
                else if(e.compareTo("XL")==0){
                    sum = sum + 40;
                    i = i + 1;
                }
                else if(e.compareTo("XC")==0){
                    sum = sum + 90;
                    i = i + 1;
                }
                else if(e.compareTo("CD")==0){
                    sum = sum + 400;
                    i = i + 1;
                }
                else if(e.compareTo("CM")==0){
                    sum = sum + 900;
                    i = i + 1;
                }
                else if(w.compareTo("I")==0){
                sum = sum + 1;
                }
                else if(w.compareTo("V")==0){
                    sum = sum + 5;
                }
                else if(w.compareTo("X")==0){
                    sum = sum + 10;
                }
                else if(w.compareTo("L")==0){
                    sum = sum + 50;
                }
                else if(w.compareTo("C")==0){
                    sum = sum + 100;
                }
                else if(w.compareTo("D")==0){
                    sum = sum + 500;
                }
                else if(w.compareTo("M")==0){
                    sum = sum + 1000;
                }
            }
            else{
                System.out.println(w);
                if(w.compareTo("I")==0){
                sum = sum + 1;
                }
                else if(w.compareTo("V")==0){
                    sum = sum + 5;
                }
                else if(w.compareTo("X")==0){
                    sum = sum + 10;
                }
                else if(w.compareTo("L")==0){
                    sum = sum + 50;
                }
                else if(w.compareTo("C")==0){
                    sum = sum + 100;
                }
                else if(w.compareTo("D")==0){
                    sum = sum + 500;
                }
                else if(w.compareTo("M")==0){
                    sum = sum + 1000;
                }
            }
        
    }
        return sum;
    }
}