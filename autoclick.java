import java.awt.Robot;
import java.awt.event.*;

public class autoclick{

    public static void main(String[] args){
        try{
            Robot r = new Robot();
            while(true){
                r.delay(5000);
                r.mouseMove(919,553);
                r.mousePress(InputEvent.BUTTON1_DOWN_MASK);
                r.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
                r.delay(800);
                r.mouseMove(783,663);
                r.mousePress(InputEvent.BUTTON1_DOWN_MASK);
                r.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
                r.delay(3000);
                r.mouseMove(810,387);
                r.mousePress(InputEvent.BUTTON1_DOWN_MASK);
                r.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
            }
        }
        catch(Exception e){
            System.out.println("dumbass");
        }
    }
}