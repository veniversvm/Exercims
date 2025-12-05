public class JedliksToyCar {
    private int battery = 100;
    private int distance = 0;
    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + this.distance + " meters";
    }

    public String batteryDisplay() {
        if (this.battery > 0){
            return "Battery at " + this.battery + "%";
        }
        return "Battery empty";
    }

    public void drive() {
        if (this.battery > 0){
            this.distance += 20;
            this.battery = battery - 1;
        }
    }
}
