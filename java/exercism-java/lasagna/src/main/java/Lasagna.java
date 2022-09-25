public class Lasagna {

    public int expectedMinutesInOven() {
        return 40;
    }

    public int remainingMinutesInOven(int minutesPassed) {
        return this.expectedMinutesInOven() - minutesPassed;
    }
    public int preparationTimeInMinutes(int layers) {
        return layers*2;
    }

    public int totalTimeInMinutes(int layers, int minutesPassed) {
        return this.preparationTimeInMinutes(layers) + minutesPassed;
    }
}
