public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        if (speed > 9 ) {
            // success 77%
            return (speed * 221) * 0.77;
        }
        if (speed > 8) {
            // 80%
            return (speed * 221) * 0.80;
        }
        if (speed > 4) {
            // 90%
            return (speed * 221) * 0.90;
        }
        return speed * 221;
    }

    public int workingItemsPerMinute(int speed) {
        return  (int) this.productionRatePerHour(speed) / 60;
    }
}
