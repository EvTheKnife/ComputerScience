import javax.swing.JFrame;

public class Main {
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();
        String myTitle = "Blank Window";
        myFrame.setTitle(myTitle);
        myFrame.setSize(300, 200);
        myFrame.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);
        myFrame.setVisible(true);
    }
}