public class DataType_002 {
    public static void main(String[] args){
        // Operating with Integer Type of Numbers
        byte myByte01 = 127;
        System.out.println("Upper Limit of Byte is: "+myByte01);
        byte myByte02 = -128;
        System.out.println("Bottom Limit of Byte is: "+myByte02);

        short myShort01 = 32767;
        System.out.println("Upper Limit of Short is: "+myShort01);
        short myShort02 = -32768;
        System.out.println("Bottom Limit of Short is: "+myShort02);

        int myInteger01 = 2147483647;
        System.out.println("Upper Limit of Integer is: "+myInteger01);
        int myInteger02 = -2147483648;
        System.out.println("Upper Limit of Integer is: "+myInteger02);

        long myLong01 = 9223372036854775807L;
        System.out.println("Upper Limit of Long is: "+myLong01);
        long myLong02 = -9223372036854775808L;
        System.out.println("Upper Limit of Long is: "+myLong02);
    }
}