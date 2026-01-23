class ReverseString {

    String reverse(String inputString) {
        String reversed = "";

        int strLength = inputString.length();

        for(int i = strLength - 1; i > -1; i--) {
            reversed = reversed + inputString.charAt(i);
        }
        
        return reversed;
        
    }
  
}
