//---------------------------------------------//
//                My Solution                  //
//---------------------------------------------//

public class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        
        return new int[] {0, 2, 5, 3, 7, 8, 4};
    }

    public int getToday() {
        return this.birdsPerDay.length > 0 ? 
            this.birdsPerDay[this.birdsPerDay.length -1] : 0;
    }

    public void incrementTodaysCount() {
        this.birdsPerDay[this.birdsPerDay.length -1] += 1;
    }

    public boolean hasDayWithoutBirds() {
        for (int day: this.birdsPerDay) {
            if (day == 0) { return true; }
            else { continue; }
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {        
        int birdCount = 0;
        for (int i=0; i<this.birdsPerDay.length && i<numberOfDays; i++) {
            birdCount += this.birdsPerDay[i];
        }
        return birdCount;
    }

    public int getBusyDays() {
        int busyDaysCount = 0;
        for (int day: this.birdsPerDay) {
            if (day >= 5) { busyDaysCount++; }
            else { continue; }
        }
        return busyDaysCount;
    }
}

//---------------------------------------------//
//          Other/Better Solutions             //
//---------------------------------------------//
/* 
Note: For the sake of brevity the code will be omitted 
      but it can be inferred from my solution

credits: https://exercism.org/tracks/java/exercises/bird-watcher/solutions/kapitanov

public boolean hasDayWithoutBirds() {
    return Arrays.stream(birdsPerDay)
        .filter(a -> a == 0)
        .findAny()
        .isPresent();
    }
public int getCountForFirstDays(int numberOfDays) {
    return Arrays.stream(birdsPerDay)
        .limit(numberOfDays)
        .sum();
    }
public int getBusyDays() {
    return (int) Arrays.stream(birdsPerDay)
        .filter(a -> a >= 5)
        .count();
    }

*/