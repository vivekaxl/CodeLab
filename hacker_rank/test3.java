import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  static int sumoR(int N, int R){
      if(N<1 || R<1) return 0;
      int sum=0;
      for(int i=1;i<=N;i++){
          sum+=i%R;
      }
      return sum;
  }

  public static void main(String[] args) {
       Scanner in = new Scanner(System.in);
       int N,R;
       int n = in.nextInt();
       int[] ar = new int[2*n];
       for(int i=0;i<2*n;i++){
          ar[i]=in.nextInt(); 
       }
       for(int i=0;i<2*n;i+=2){
         N = ar[i];
         R = ar[i+1];
         System.out.println(sumoR(N,R));
       }
   }   
}
