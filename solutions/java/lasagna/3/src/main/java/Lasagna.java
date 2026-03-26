public class Lasagna {
    public int expectedMinutesInOven(){
        return 40;
    }

    public int remainingMinutesInOven(int actualMin) {
        return expectedMinutesInOven() - actualMin;
    }

    public int preparationTimeInMinutes(int layers) {
        return layers * 2;
    }

    public int totalTimeInMinutes(int layers, int minutes) {
        return this.preparationTimeInMinutes(layers) + minutes;
    }
}
