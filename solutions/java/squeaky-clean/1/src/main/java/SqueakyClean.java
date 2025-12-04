class SqueakyClean {
    static String clean(String identifier) {
        
        return toNormalText(toCamelCase(identifier.replace(' ', '_')));
    }

    // recursive solution to the camelCase
    static String toCamelCase(String s){
        int index =s.indexOf("-");
        if (index > -1){
            char[] sArray = s.toCharArray();
            sArray[index+1] = Character.toUpperCase(sArray[index+1]); 
            String newString = new String(sArray);
            return toCamelCase(newString.replace("-", ""));
        } 
        return s;
    }

    static String toNormalText(String s){
        return s.replace('4', 'a')
            .replace('3', 'e')
            .replace('0', 'o')
            .replace('1', 'l')
            .replace('7', 't')
            // here I extended the method to accomplish the task 4
            .replace("!", "")
            .replace("¡", "")
            .replace("$", "")
            .replace(".", "")
            .replace("#", "");
    }

}
