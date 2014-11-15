import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  static int isPrime(int num){
      if(num%2 == 0) return 0;
      for(int i=2;i<=num/2;i++){
          if(num%i == 0) return 0;
      }
      return 1;
  }

  public static void main(String[] args) {
       Scanner in = new Scanner(System.in);
       int N,R;
       int n = in.nextInt();
       int[] ar = new int[n];
       for(int i=0;i<n;i++){
          ar[i]=in.nextInt(); 
       }
       for(int i=0;i<n;i++){
         if(isPrime(ar[i])==0) System.out.println("NO");
         else System.out.println("YES");
       }
   }   
}
