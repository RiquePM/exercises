class ProductionRemoteControlCar implements RemoteControlCar, Comparable<ProductionRemoteControlCar> {

    private int distanceTravelled;
    private int numberofVictories;

    public void drive() {
        this.distanceTravelled += 10;
    }

    public int getDistanceTravelled() {
        return this.distanceTravelled;
    }

    public int getNumberOfVictories() {
        return this.numberofVictories;
    }

    public void setNumberOfVictories(int numberofVictories) {
        this.numberofVictories = numberofVictories;
    }

    //@Override 
    public int compareTo(ProductionRemoteControlCar car) {
        // -1: less than
        // 0: equal
        // 1: greater than
        return this.getDistanceTravelled() > car.getDistanceTravelled() ? 
            1 : 
            this.getDistanceTravelled() < car.getDistanceTravelled() ? 
                -1 : 
                0;

        /* ----------------
          |Better solution|
          -----------------
          Credits: https://exercism.org/tracks/java/exercises/remote-control-competition/solutions/danieldietrich

          return this.numberOfVictories - that.getNumberOfVictories();
        */

    }
}
