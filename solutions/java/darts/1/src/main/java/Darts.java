class Darts {
    int score(double xOfDart, double yOfDart) {
        double point = Math.pow(xOfDart, 2) + Math.pow(yOfDart, 2); 

        if (point > 100)
            return 0;
        if (point > 25)
            return 1;
        if (point > 1)
            return 5;
        return 10;
    }
}
