import static java.util.Map.entry;

import java.util.Map;


public class CarsAssemble {
    private final int CARS_PRODUCED_AT_LOWEST_SPEED = 221;
    Map<Integer, Double> SUCCESS_RATE = Map.ofEntries(
        entry(0, 0.0), entry(1, 1.0), entry(2, 1.0),
        entry(3, 1.0), entry(4, 1.0), entry(5, 0.9),
        entry(6, 0.9), entry(7, 0.9), entry(8, 0.9),
        entry(9, 0.8), entry(10, 0.77)
    );

    public double productionRatePerHour(int speed) {
        return (speed*this.CARS_PRODUCED_AT_LOWEST_SPEED)
            *SUCCESS_RATE.get(speed);
    }

    public int workingItemsPerMinute(int speed) {
        return (int) productionRatePerHour(speed)/60;
    }
}
