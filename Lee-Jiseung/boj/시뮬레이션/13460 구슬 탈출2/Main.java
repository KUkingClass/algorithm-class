import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    static int[] dr = {-1, 1, 0, 0}; // 상 하 좌 우
    static int[] dc = {0, 0, -1, 1};

    private static class Board {
        public int[] red;
        public int[] blue;

        public Board() {
            this.red = new int[2];
            this.blue = new int[2];
        }

        public Board(int a, int b, int c, int d) {
            this.red = new int[] {a, b};
            this.blue = new int[] {c, d};
        }

        private boolean isRedAndBlueStandSameLocation() {
            if ((this.red[0] == this.blue[0]) && (this.red[1] == this.blue[1])) {
                return true;
            }
            return false;
        }

        private void moveRed(int i) {
            this.red[0] += dr[i];
            this.red[1] += dc[i];
        }
        private void moveBackRed(int i) {
            this.red[0] -= dr[i];
            this.red[1] -= dc[i];
        }

        private void moveBlue(int i) {
            this.blue[0] += dr[i];
            this.blue[1] += dc[i];
        }
        private void moveBackBlue(int i) {
            this.blue[0] -= dr[i];
            this.blue[1] -= dc[i];
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] grid = new int[n][m];
        Board board = new Board();

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < m; j++) {
                if (s.charAt(j) == '#') {
                    grid[i][j] = -1;
                }else if (s.charAt(j) == 'R') {
                    board.red[0] = i;
                    board.red[1] = j;
                }
                else if (s.charAt(j) == 'B') {
                    board.blue[0] = i;
                    board.blue[1] = j;
                }
                else if (s.charAt(j) == 'O') {
                    grid[i][j] = 1;
                }
            }
        }

        List<Board> dq = new ArrayList<>();
        dq.add(board);

        for (int iter = 1; iter <= 10; iter++) {
            List<Board> new_dq = new ArrayList<>();
            
            for (int i = 0; i < 4; i++) {
                for (Board b : dq) {
                    Board temp_board = new Board(b.red[0], b.red[1], b.blue[0], b.blue[1]);
                    int blue_flag = 0, red_flag = 0;

                    while (true) {
                        temp_board.moveBlue(i);
                        if (grid[temp_board.blue[0]][temp_board.blue[1]] == 1) {
                            blue_flag = 1;
                            break;
                        } else if (grid[temp_board.blue[0]][temp_board.blue[1]] == -1) {
                            blue_flag = -1;
                            temp_board.moveBackBlue(i);
                            break;
                        } else if (temp_board.isRedAndBlueStandSameLocation()) {
                            temp_board.moveBackBlue(i);
                            break;
                        }
                    }

                    if (blue_flag == 1) {
                        continue;
                    }

                    while (true) {
                        temp_board.moveRed(i);
                        if (grid[temp_board.red[0]][temp_board.red[1]] == 1) {
                            red_flag = 2;
                            break;
                        } else if (grid[temp_board.red[0]][temp_board.red[1]] == -1 || temp_board.isRedAndBlueStandSameLocation()) {
                            temp_board.moveBackRed(i);
                            break;
                        }
                    }

                    if (blue_flag == 0) {
                        while (true) {
                            temp_board.moveBlue(i);
                            if (grid[temp_board.blue[0]][temp_board.blue[1]] == 1) {
                                red_flag = -1;
                                break;
                            } else if (grid[temp_board.blue[0]][temp_board.blue[1]] == -1 || temp_board.isRedAndBlueStandSameLocation()) {
                                temp_board.moveBackBlue(i);
                                break;
                            }
                        }
                    }

                    if (red_flag == 2) {
                        bw.write(String.valueOf(iter));
                        bw.flush();
                        return;
                    } else if (red_flag == -1) {
                        continue;
                    }

                    new_dq.add(new Board(temp_board.red[0], temp_board.red[1], temp_board.blue[0], temp_board.blue[1]));
                }
            }
            dq = new_dq;
        }

        bw.write(String.valueOf(-1));
        bw.flush();
    }
}
