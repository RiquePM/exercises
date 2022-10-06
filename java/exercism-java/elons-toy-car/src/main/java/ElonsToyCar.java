public class ElonsToyCar {
    
    private int totalDistance = 0;
    private int battery = 100;
    
    public static ElonsToyCar buy() {
        return new ElonsToyCar();
    }

    public String distanceDisplay() {
        return String.format(
            "Driven %d meters", this.totalDistance
        );
    }

    public String batteryDisplay() {
        return this.battery == 0 ? 
            "Battery empty" : 
            String.format("Battery at %d%%", this.battery);
    }

    public void drive() {
        if (!(this.totalDistance == 2000 || this.battery == 0)) {
            this.totalDistance += 20;
            this.battery -= 1;
        }
    }
}
