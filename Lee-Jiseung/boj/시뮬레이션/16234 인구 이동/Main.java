import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;
import java.util.jar.JarEntry;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int[][] population = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                population[i][j] = Integer.parseInt(st2.nextToken());
            }
        }

        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};

        int answer = 0;
        boolean flag = true;
        while (flag) {
            answer++;
            flag = false;

            List<List<Integer>> unions = new ArrayList<>();
            boolean[][] visited = new boolean[n][n];
            List<Integer> dq = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (visited[i][j]) {
                        continue;
                    }

                    List<Integer> union = new ArrayList<>();
                    dq.add(i * n + j);

                    while (dq.size() > 0) {
                        int cur = dq.remove(0);
                        int x = cur / n;
                        int y = cur % n;

                        if (visited[x][y]) {
                            continue;
                        }
                        visited[x][y] = true;
                        union.add(x * n + y);

                        for (int k = 0; k < 4; k++) {
                            int newx = x + dr[k];
                            int newy = y + dc[k];
                            if (newx < 0 || newx >= n || newy < 0 || newy >= n) {
                                continue;
                            }

                            int diff = Math.abs(population[newx][newy] - population[x][y]);
                            if (!visited[newx][newy] && l <= diff && diff <= r) {
                                dq.add(newx * n + newy);
                            }
                        }
                    }

                    unions.add(union);
                }
            }

            for (List<Integer> union : unions) {
                if (union.size() == 1) {
                    continue;
                }

                int average = 0;
                for (Integer loc : union) {
                    int x = loc / n;
                    int y = loc % n;
                    average += population[x][y];
                }
                average /= union.size();

                for (Integer loc : union) {
                    int x = loc / n;
                    int y = loc % n;
                    if (population[x][y] != average) {
                        flag = true;
                    }
                    population[x][y] = average;
                }
            }
        }

        bw.write(String.valueOf(answer-1));
        bw.flush();
    }
}
