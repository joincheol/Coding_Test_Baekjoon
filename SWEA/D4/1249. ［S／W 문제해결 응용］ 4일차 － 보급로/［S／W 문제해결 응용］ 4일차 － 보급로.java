/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    static final int INF = Integer.MAX_VALUE;
    static int n;
    static int[][] map;
    static int[][] dist;
    static boolean[][] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    
	public static void main(String args[]) throws Exception
	{
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        for(int tc=1; tc<=t; tc++){
        	n = sc.nextInt();
            
            map = new int[n][n];
            dist = new int[n][n];
            visited = new boolean[n][n];
            for(int i=0; i<n; i++){
            	String line = sc.next();
                char[] c = line.toCharArray();
                for(int j=0; j<n; j++){
                	map[i][j] = c[j] - '0';
                    dist[i][j] = INF;
                }
            }
            
            int answer = dijkstra(0, 0);
            
            System.out.println("#"+tc+" "+answer);
        }
	}
    static int dijkstra(int r, int c){
        dist[r][c] = 0;
        
        for(int cnt=0; cnt<n*n; cnt++){
        	int minDist = INF;
            int curR = -1;
            int curC = -1;
            
            for(int i=0; i<n; i++){
            	for(int j=0; j<n; j++){
                	if(!visited[i][j] && dist[i][j] < minDist){
                    	curR = i;
                        curC = j;
                        minDist = dist[i][j];
                    }
                }
            }
            if(curR == -1 || curC == -1){
            	break;
            }
            visited[curR][curC] = true;
            if(curR == n-1 && curC == n-1){
            	return dist[curR][curC];
            }
            
            
            for(int d=0; d<4; d++){
            	int nr = curR + dr[d];
                int nc = curC + dc[d];
                
                if(nr < 0 || nr >=n || nc < 0 || nc >= n){
                	continue;
                }
                if(visited[nr][nc]){
                	continue;
                }
                
                int newDist = dist[curR][curC] + map[nr][nc];
                if(newDist < dist[nr][nc]){
                	dist[nr][nc] = newDist;
                }
            }
        }
        
    	return dist[n-1][n-1];
    }
}