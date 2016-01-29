import java.util.Scanner; import java.util.regex.*;

public class Solution {
 public static void main(String[] args){
  	Scanner in = new Scanner(System.in);
   	int testCases = Integer.parseInt(in.nextLine());
    while(testCases>0){
    	String pattern = in.nextLine();
      	int flag=1;
      	String pattern1 = pattern.replaceAll("\s","");
        try{ 
        	Pattern.compile(pattern1);
         	flag=1;
        } 
        catch(Exception e) { 
          flag=0;
		}

        if(flag==0)
        	System.out.println("Invalid");
        else 
            System.out.println("Valid");
        testCases--;
	} 
	
	}
}