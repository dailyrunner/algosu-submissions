import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N,M;
    static boolean[][] map;
    static int[][] answer;
    static int[][] p;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};

    public static void main(String[] args) throws IOException{
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        map = new boolean[N][M];
        answer = new int[N][M];
        
        for(int i=0;i<N;i++){
            String temp = br.readLine();
            for(int j=0;j<M;j++){
                if(temp.charAt(j)=='1'){
                    map[i][j] = true;
                }
            }
        }

        p = new int[N*M][2]; // 조상 추적 + 개수 count 용 배열
        for(int i=0;i<N*M;i++){
            p[i][0] = i; // root
            p[i][1] = 1; // 개수
        }

        
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(map[i][j]) continue; // 0이 아니면, 즉 벽이면 건너뛰기
                for(int k=0;k<4;k++){
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if(nx<0||ny<0||nx>=N||ny>=M) continue; // 범위에서 벗어난 좌표이면 건너 뛰기
                    if(map[nx][ny]) continue; // 0이 아니면, 즉 벽이면 건너뛰기
                    union(serialize(i, j), serialize(nx, ny));
                }
            }
        }


        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(!map[i][j]) continue; // 벽이 아니면 건너뛰기
                int sum = 1;
                int[] roots = new int[4];
                for(int k=0;k<4;k++){
                    roots[k] = -1;
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if(nx<0||ny<0||nx>=N||ny>=M) continue; // 범위에서 벗어난 좌표이면 건너 뛰기
                    if(map[nx][ny]) continue; // 0이 아니면, 즉 벽이면 건너뛰기
                    roots[k] = findRoot(serialize(nx, ny));
                    boolean didWeCount = false;
                    for(int l=0;l<k;l++){
                        if(roots[k]==roots[l]){
                            didWeCount = true;
                            break;
                        }
                    }
                    if(didWeCount) continue;
                    sum += p[roots[k]][1];
                }
                answer[i][j] = sum;
            }
        }

        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                sb.append(answer[i][j]%10);
            }
            sb.append("\n");
        }
        
        System.out.println(sb);
    }

    public static int findRoot(int x){
        if(p[x][0]==x) return x;
        return p[x][0] = findRoot(p[x][0]);
    }

    public static void union(int a, int b){
        int rootA = findRoot(a);
        int rootB = findRoot(b);

        if(rootA==rootB) return;

        p[rootB][0] = rootA;
        p[rootA][1] += p[rootB][1];
        p[rootB][1] = 0;
    }

    public static int serialize(int x, int y){
        return x*M + y;
    }
}
