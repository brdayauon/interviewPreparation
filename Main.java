import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class Main 
{
	private static final int BOARD_SIZE = 9;
	private static int steps = 0;
	
	public static void main(String args[])
    {
        String testVal = "341205678";

        Scanner sc = new Scanner(System.in);

        System.out.print("Do you want to (1) Generate a random puzzle problem OR (2) Enter a specific configuration: ");
        int input = sc.nextInt();

        if (input == 1) {
            System.out.println("Random Board: ");
            Board randomBoard = new Board(1);
            testVal = randomBoard.getState();
            
            Board randomBoardH1 = new Board(testVal, 0, 1); // heuristic 1
            Board randomBoardH2 = new Board(testVal, 0, 2); // heuristic 2
            
            System.out.println("\nInitial State: ");
            System.out.println(randomBoard);

            System.out.println("\nHeuristic 1 using TREE BFS: ");
            bestFirstSearch(randomBoardH1);

            System.out.println("\nHeuristic 2 using TREE BFS: ");
            bestFirstSearch(randomBoardH2);

            System.out.println("\nHeuristic 1 using GRAPH A*: ");
            Node result = aStarSearch(randomBoardH1);

            System.out.println("\nHeuristic 2 using GRAPH A*: ");
            Node result2 = aStarSearch(randomBoardH2);
        }
        if (input == 2) {
            String puzzleInput = "";
            System.out.println("Enter a puzzle. In this format for example (no spaces): 124056837");
            //System.out.println("Enter your puzzle: ");
          //  sc.next();
            puzzleInput = sc.nextLine();  // Read user input


            while(puzzleInput.length() != 9) {
                if(puzzleInput.length() != 9) {
                    System.out.println("Must have 9 unique numbers in your puzzle ");
                    System.out.println("Enter your puzzle: ");
                    puzzleInput = sc.nextLine();  // Read user input
                }
            }

            testVal = puzzleInput;
            
            Board testBoard = new Board(testVal, 0, 1); // heuristic 1
            Board testBoardH2 = new Board(testVal, 0, 2); // heuristic 2

            System.out.println("\nInitial State: ");
            System.out.println(testBoard);

            System.out.println("\nHeuristic 1 using TREE BFS: ");
            bestFirstSearch(testBoardH2);

            System.out.println("\nHeuristic 2 using TREE BFS: ");
            bestFirstSearch(testBoardH2);

            System.out.println("\nHeuristic 1 using GRAPH A*: ");
            Node result = aStarSearch(testBoard);
         //   System.out.println("DEPTH: " + result.getBoard().getDepth());

            System.out.println("\nHeuristic 2 using GRAPH A*: ");
            Node result2 = aStarSearch(testBoardH2);
        }

    }
	
	public static Board bestFirstSearch(Board testBoard)
	{
		boolean isSuccess = false;
		PriorityQueue<Board> queue = new PriorityQueue<Board>();
		HashSet<String> explored = new HashSet<String>();
		queue.add(testBoard);
		while (!queue.isEmpty() && !isSuccess) 
		{
			Board n = queue.peek();
			explored.add(n.getState());
			
			System.out.println(n); // Prints out the current state
			
			if (n.getState().equals("012345678")) {
				isSuccess = true;
				return n;
			}
			n = queue.remove();
			ArrayList<Board> children = n.generateChildren(explored);
			for (int i = 0; i < children.size(); i++) {
				children.get(i).increaseDepth();
				queue.add(children.get(i));
			}
		}
		return null;
	}
	
	public static Node aStarSearch(Board testBoard)
	{
		boolean isSuccess = false;
		int steps = 0;
		Node firstNode = new Node(testBoard, 0);
		PriorityQueue<Node> frontier = new PriorityQueue<Node>();
		frontier.add(firstNode);
		HashSet<String> explored = new HashSet<String>();
		
		while (!isSuccess) {
			steps++;
			if (frontier.isEmpty()) {
				break;
			}
			Node n = frontier.remove();
			System.out.println(n.getBoard());
			if (n.getBoard().getState().equals("012345678")) {
				return n;
			}
			if (steps > 10000)
				break;
			explored.add(n.getBoard().getState());
			ArrayList<Board> children = n.getBoard().generateChildren(explored);
			
			for (int i = 0; i < children.size(); i++) {
				children.get(i).increaseDepth();
				frontier.add(new Node(children.get(i), 0));
			}
		}
		return null;
	}
	
}
