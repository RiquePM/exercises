//---------------------------------------------//
//                My Solution                  //
//---------------------------------------------//

class NeedForSpeed {

    int speed;
    private int batteryDrain;
    private int battery = 100;
    private int distanceDriven = 0;

    public NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
    }

    public boolean batteryDrained() {
        return this.battery == 0 ? true : false;
    }

    public int distanceDriven() {
        return this.distanceDriven;
    }

    public void drive() {
        if (!(batteryDrained())) {
            this.distanceDriven += this.speed;
            this.battery -= this.batteryDrain;            
        }
    }

    public static NeedForSpeed nitro() {
        return new NeedForSpeed(50, 4);
    }
}

class RaceTrack {
    
    int distance;

    public RaceTrack(int distance) {
        this.distance = distance;
    }

    public boolean tryFinishTrack(NeedForSpeed car) {
        for (int i=0; i<(this.distance/car.speed); i++) {
            car.drive();
            if (car.batteryDrained() && car.distanceDriven() < this.distance) {
                return false;
            }
        }
        return true;
    }
}


//---------------------------------------------//
//          Other/Better Solutions             //
//---------------------------------------------//
/* 
Note: For the sake of brevity the code will be omitted 
      but it can be inferred from my solution

credits: https://exercism.org/tracks/java/exercises/need-for-speed/solutions/heptalophos

public boolean tryFinishTrack(NeedForSpeed car) {
    return distance <= 100 * car.getSpeed() / car.getBatteryDrain();
}



*/