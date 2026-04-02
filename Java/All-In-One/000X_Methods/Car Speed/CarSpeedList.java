import java.util.Scanner;

public class CarSpeedList {
    public static void inputSpeed(int[] speed) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input a Speed (between 1 and 300 km/h, -1 to end):");
        
        int index = 0;
        while (index < speed.length) {
            int input = scanner.nextInt();
            
            if (input == -1) {
                break; // End of loop if the input is -1
            }
            
            if (input >= 1 && input <= 300) {
                speed[index] = input;
                index++;
            }
            else
            {
                System.out.println("Invalid Speed. Please input again");
            }
        }
    }
    
    public static void outputSpeed(int[] speed) {
        if (speed == null) {
            System.out.println("No Speed was given");
            return;
        }
        
        System.out.println("Given Speeds: ");
        boolean hasValues = false;
        for (int speed_0 : speed) {
            if (speed_0 > 0) {
                System.out.println("Speed: " + speed_0 + " km/h");
                hasValues = true;
            }
            if (!hasValues) {
                System.out.println("No valid speed was given.");
            }
        }
    }
    
    public static void main(String[] args) {
        int[] speed = new int[10];
        inputSpeed(speed);
        outputSpeed(speed);
    }
}