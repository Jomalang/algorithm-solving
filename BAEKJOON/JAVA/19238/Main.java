import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int M;
    static long fuels;
    static List<List<Integer>> map;
    static Coordi cur;
    static List<List<Coordi>> passengers;

    public static void main(String[] args) throws IOException {
        System.out.println("Hello World");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr1 = br.readLine().split(" ");
        N = Integer.parseInt(arr1[0]);
        M = Integer.parseInt(arr1[1]);
        fuels = Long.parseLong(arr1[2]);

        map = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] tmp = br.readLine().split(" ");
            int[] tmp2 = Arrays.stream(tmp).mapToInt(Integer::parseInt).toArray();
            map.add(new ArrayList<>());
            for (int j = 0; j < N; j++) {
                map.get(i).add(tmp2[j]);
            }
        }

        int[] startCoordi = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        cur = new Coordi(startCoordi[0], startCoordi[1]);

        passengers = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            int[] tmp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            passengers.add(new ArrayList<>());
            for (int j = 0; j < 4; j += 2) {
                passengers.get(i).add(new Coordi(tmp[j], tmp[j + 1]));
            }
        }

    }

    static void solution() {

    }

    static class Coordi {
        int row;
        int col;

        public Coordi(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}