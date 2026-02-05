class ArmstrongNumbers {

    boolean isArmstrongNumber(int numberToCheck) {

        String numberStr = String.valueOf(numberToCheck);
        int pow = numberStr.length();
        int isArmstrong = 0;

        for (char ch : numberStr.toCharArray()){
            isArmstrong += Math.pow(Character.getNumericValue(ch), pow);
        }

        return isArmstrong == numberToCheck;

    }

}
