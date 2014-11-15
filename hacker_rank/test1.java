import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  static int sumDigits(int num){
      int sum=0;
      while(num>0){
          sum+=num%10;
          num/=10;
      }
      return sum;
  }

  public static void main(String[] args) {
       Scanner in = new Scanner(System.in);
       int n = in.nextInt();
       int[] ar = new int[n];
       for(int i=0;i<n;i++){
          ar[i]=in.nextInt(); 
       }
       for(int i=0;i<n;i++)
         System.out.println(sumDigits(ar[i]));
   }   
}
