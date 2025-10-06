import java.util.*;

public class DataGenerator {
    public static List<Integer> generateData(int n) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(i * i + 3);
        }
        return list;
    }

    public static void printStats(List<Integer> data) {
        int sum = 0;
        for (int d : data) sum += d;
        double avg = (double) sum / data.size();
        System.out.println("Average: " + avg);
    }

    public static void main(String[] args) {
        List<Integer> data = generateData(50);
        printStats(data);
    }
}

