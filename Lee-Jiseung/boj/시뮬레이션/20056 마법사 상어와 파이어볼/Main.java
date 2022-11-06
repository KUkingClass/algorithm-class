import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    static int n;
    static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dc = {0, 1, 1, 1, 0, -1, -1, -1};
    static int[] directions = {0, 2, 4, 6};

    static public class Shark {
        List<Fireball> fireballs;

        public Shark() {
            this.fireballs = new ArrayList<>();
        }

        void addFireball(Fireball fireball) {
            this.fireballs.add(fireball);
        }

        void move() {
            for (Fireball fireball : fireballs) {
                fireball.move();
            }
        }

        void afterMove() {
            boolean[] flags = new boolean[fireballs.size()];
            List<Fireball> new_fireballs = new ArrayList<>();

            for (int i = 0; i < fireballs.size(); i++) {
                if (flags[i]) {
                    continue;
                }
                int ri = fireballs.get(i).r, ci = fireballs.get(i).c;
                List<Integer> indexes = new ArrayList<>();
                
                for (int j = i+1; j < fireballs.size(); j++) {
                    if (flags[i]) {
                        continue;
                    }

                    if (ri != fireballs.get(j).r || ci != fireballs.get(j).c) {
                        continue;
                    }

                    indexes.add(j);
                }

                if (indexes.size() == 0) {
                    continue;
                }
                indexes.add(0, i);

                for (Integer index : indexes) {
                    flags[index] = true;
                }

                List<Integer> msd = getMSD(indexes);

                if (msd.get(0) == 0) {
                    continue;
                }

                new_fireballs.addAll(divideFireball(Arrays.asList(ri, ci, msd.get(0), msd.get(1), msd.get(2))));
            }

            for (int i = 0; i < flags.length; i++) {
                if (flags[i]) {
                    continue;
                }
                new_fireballs.add(fireballs.get(i));
            }

            fireballs = new_fireballs;
        }

        private List<Integer> getMSD(List<Integer> indexes) {
            int sum_mass = 0;
            int sum_speed = 0;
            int count_odd_direction = 0;
            for (Integer index : indexes) {
                sum_mass += fireballs.get(index).mass;
                sum_speed += fireballs.get(index).speed;
                if (fireballs.get(index).direction % 2 == 1) {
                    count_odd_direction++;
                }
            }

            return Arrays.asList(sum_mass / 5, sum_speed / indexes.size(), (count_odd_direction % indexes.size() == 0) ? 0 : 1);
        }

        private List<Fireball> divideFireball(List<Integer> infos) {
            List<Fireball> temp_fireballs = new ArrayList<>();
            for (int i = 0; i < 4; i++) {
                temp_fireballs.add(new Fireball(infos.get(0), infos.get(1), infos.get(2), infos.get(3), directions[i] + infos.get(4)));
            }
            return temp_fireballs;
        }

        int getTotalMass() {
            int sum = 0;
            for (Fireball fireball : fireballs) {
                sum += fireball.mass;
            }
            return sum;
        }
    }

    static public class Fireball {
        int r, c, mass, speed, direction;

        public Fireball(String line) {
            String[] s = line.split(" ");
            this.r = Integer.parseInt(s[0]) - 1;
            this.c = Integer.parseInt(s[1]) - 1;
            this.mass = Integer.parseInt(s[2]);
            this.speed = Integer.parseInt(s[3]);
            this.direction = Integer.parseInt(s[4]);
        }

        public Fireball(int r, int c, int m, int s, int d) {
            this.r = r;
            this.c = c;
            this.mass = m;
            this.speed = s;
            this.direction = d;
        }

        void move() {
            r = (r + dr[direction] * speed) % n;
            c = (c + dc[direction] * speed) % n;
            while (r < 0) {
                r += n;
            }
            while (c < 0) {
                c += n;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Shark shark = new Shark();
        for (int i = 0; i < m; i++) {
            shark.addFireball(new Fireball(br.readLine()));
        }

        for (int i = 0; i < k; i++) {
            shark.move();
            shark.afterMove();
        }

        bw.write(String.valueOf(shark.getTotalMass()));
        bw.flush();
    }
}
