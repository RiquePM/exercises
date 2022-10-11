import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TestTrack {

    public static void race(RemoteControlCar car) {
        car.drive();
    }

    public static List<ProductionRemoteControlCar> getRankedCars(
        ProductionRemoteControlCar prc1, ProductionRemoteControlCar prc2) {
            
            List<ProductionRemoteControlCar> ranked_cars = 
                new ArrayList<ProductionRemoteControlCar>(); 
            ranked_cars.add(prc1);
            ranked_cars.add(prc2);
            Collections.reverse(ranked_cars);
            return ranked_cars;
    }
}
