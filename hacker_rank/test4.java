import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  static int count(int num){
      int count=0;
      while(num>0){
          if(num%2 == 1) count++;
          num/=2;
      }
      return count;
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
         System.out.println(count(ar[i]));
       }
   }   
}
