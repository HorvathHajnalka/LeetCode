//allows for the modification and construction of character strings without the need to create new strings every time
public class StringBuilderExample{
    public static void main(String[] args) {

        //string builder class
        StringBuilder sb = new StringBuilder();
        //append
        sb.append("Hello");
        sb.append(", ");
        sb.append("World!");
        //setCharAt
        sb.setCharAt(0, 'h');
        //toString
        String result = sb.toString();
        //result
        System.out.println(result);

    }
}