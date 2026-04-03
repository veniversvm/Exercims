
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        return this.birdsPerDay;
    }

    public int getToday() {
        return birdsPerDay[ birdsPerDay.length -1];
    }

    public void incrementTodaysCount() {
        int pos = birdsPerDay.length -1;
        int newValue = birdsPerDay[pos] + 1;
        birdsPerDay[pos] = newValue;
    }

    public boolean hasDayWithoutBirds() {
        for (int birds : birdsPerDay) {
            if (birds == 0)
                return true;
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int count = 0;
        numberOfDays = numberOfDays > 7 ? 7 : numberOfDays;
        
        for (int i = 0; i < numberOfDays; i++) {
            count += birdsPerDay[i];
        }

        return count;
    }

    public int getBusyDays() {
        int count = 0;
        for (int birds : birdsPerDay) {
            if (birds > 4)
                count++;
        }
        return count;
    }
}
