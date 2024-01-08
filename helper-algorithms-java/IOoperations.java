import java.io.*;

//keyboard input
class Main{
	public static void main(String[] args) {
		BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in)); 
		try{
			String input = keyboard.readLine();
		}catch(IOException ex){
			ex.printStackTrace();
		}
	}
};

//file input
class Main{
	public static void main(String[] args) {
		try{
			BufferedReader inFile = new BufferedReader(new FileReader("data.txt")); 
			String input = inFile.readLine(); 
			//tobb sor
			String input = null;
			int count = 0;
			while ((input = inFile.readLine())!= null){  //tobb soros file input
				size = Double.valueOf(input); //...
			}
			
		}catch(IOException ex){
			ex.printStackTrace();
		}
	}
};

//file output
class Main{
	public static void main(String[] args) {
		PrintWriter outFile = null;
		try{
			outFile = new PrintWriter("output.txt");
			outFile.println("hello");
		}catch(IOException ex){
			ex.printStackTrace();
		}finally{
			if(outFile != null )outFile.close(); 
		}
	}
};