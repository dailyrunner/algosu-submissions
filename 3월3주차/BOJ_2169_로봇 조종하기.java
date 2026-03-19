import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N,M;
    static int[][] map;
    static int[][] d;

    public static void main(String[] args) throws IOException{
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        map = new int[N][M];
        d = new int[N][M];
        for(int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<M;j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        d[0][0] = map[0][0];
        for(int j=1;j<M;j++){
            d[0][j] = d[0][j-1] + map[0][j];
        }

        for(int i=1;i<N;i++){
            // 왼쪽에서 오른쪽으로 가는 경우를 저장할 배열
            int[] leftToRight = new int[M];
            int[] rightToLeft = new int[M];

            leftToRight[0] = d[i-1][0] + map[i][0];
            for(int j=1;j<M;j++){
                leftToRight[j] = Math.max(d[i-1][j], leftToRight[j-1]) + map[i][j];
            }

            rightToLeft[M-1] = d[i-1][M-1] + map[i][M-1];
            for(int j=M-2;j>=0;j--){
                rightToLeft[j] = Math.max(d[i-1][j], rightToLeft[j+1]) + map[i][j];
            }

            for(int j=0;j<M;j++){
                d[i][j] = Math.max(leftToRight[j],rightToLeft[j]);
            }
        }

        System.out.println(d[N - 1][M - 1]);
    }
}
