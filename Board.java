import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;

public class Board implements Comparable<Board>
{
	private static final int BOARD_SIZE = 9;
	private int depth;
	private String state;
	private int heuristic;
	
	public Board(int heuristic) // WILL GENERATE RANDOM STATE AT DEPTH 0
	{
		setRandomWorkingPuzzle();
		this.depth = 0;
		this.heuristic = heuristic;
	}
	
	public Board(String state, int depth, int heuristic)
	{
		this.state = state;;
		this.depth = depth;
		this.heuristic = heuristic;
	}
	
	public String getState()
	{
		return state;
	}
	
	public Board swap(int pos1, int pos2)
	{
		StringBuilder sb = new StringBuilder(state); 
        sb.setCharAt(pos1, state.charAt(pos2));
        sb.setCharAt(pos2, state.charAt(pos1));
        return new Board(sb.toString(), depth, heuristic); 
	}
	
	public ArrayList<Board> generateChildren(HashSet<String> explored)
	{
		ArrayList<Board> children = new ArrayList<Board>();
		
		if (getEmptyPosition() == 0) {
			if (!explored.contains(this.swap(0,1).getState()))
				children.add(this.swap(0,1));
			if (!explored.contains(this.swap(0,3).getState()))
				children.add(this.swap(0,3));
		}
		else if (getEmptyPosition() == 1) {
			if (!explored.contains(this.swap(1,0).getState()))
				children.add(this.swap(1,0));
			if (!explored.contains(this.swap(1,2).getState()))
				children.add(this.swap(1,2));
			if (!explored.contains(this.swap(1,4).getState()))
				children.add(this.swap(1,4));
		}
		else if (getEmptyPosition() == 2) {
			if (!explored.contains(this.swap(2,1).getState()))
				children.add(this.swap(2,1));
			if (!explored.contains(this.swap(2,5).getState()))
				children.add(this.swap(2,5));
		}
		else if (getEmptyPosition() == 3) {
			if (!explored.contains(this.swap(3,0).getState()))
				children.add(this.swap(3,0));
			if (!explored.contains(this.swap(3,4).getState()))
				children.add(this.swap(3,4));
		}
		else if (getEmptyPosition() == 4) {
			if (!explored.contains(this.swap(4,1).getState()))
				children.add(this.swap(4,1));
			if (!explored.contains(this.swap(4,3).getState()))
				children.add(this.swap(4,3));
			if (!explored.contains(this.swap(4,5).getState()))
				children.add(this.swap(4,5));
			if (!explored.contains(this.swap(4,7).getState()))
				children.add(this.swap(4,7));
		}
		else if (getEmptyPosition() == 5) {
			if (!explored.contains(this.swap(5,2).getState()))
				children.add(this.swap(5,2));
			if (!explored.contains(this.swap(5,4).getState()))
				children.add(this.swap(5,4));
			if (!explored.contains(this.swap(5,8).getState()))
				children.add(this.swap(5,8));
		}
		else if (getEmptyPosition() == 6) {
			if (!explored.contains(this.swap(6,3).getState()))
				children.add(this.swap(6,3));
			if (!explored.contains(this.swap(6,7).getState()))
				children.add(this.swap(6,7));
		}
		else if (getEmptyPosition() == 7) {
			if (!explored.contains(this.swap(7,4).getState()))
				children.add(this.swap(7,4));
			if (!explored.contains(this.swap(7,6).getState()))
				children.add(this.swap(7,6));
			if (!explored.contains(this.swap(7,8).getState()))
				children.add(this.swap(7,8));
		}
		else if (getEmptyPosition() == 8) {
			if (!explored.contains(this.swap(8,5).getState()))
				children.add(this.swap(8,5));
			if (!explored.contains(this.swap(8,7).getState()))
				children.add(this.swap(8,7));
		}
		
		return children;
	}
	
	public void setRandomWorkingPuzzle() {
		boolean valid = false;
		state = "";
		while (!valid) {
			List<Integer> list = new LinkedList<Integer>();
		    for (int i = 0; i < BOARD_SIZE; i++) {
		    	list.add(i);
		    }
		    Collections.shuffle(list);
		    for (int i = 0; i < BOARD_SIZE; i++) {
		    	state+=list.get(i);
		    }
		    if (this.isSolvable())
		    	valid = true;
		    else
		    	state = "";
		}
	}
	
	public int getEmptyPosition()
	{
		for (int i = 0; i < state.length(); i++) {
		    if (state.charAt(i) == '0')
		    	return i;
		    //Process char
		}
		return -1; // there is no empty space
	}
	
	public int getMisplacedTiles()
	{
		int misplaced = 0;
		for (int i = 0; i < state.length(); i++) {
			if (i != Integer.parseInt(String. valueOf(state.charAt(i))))
				misplaced++;
		}
		return misplaced;
	}

	public int getManhattanEval()
	{
		int[] intArray = new int[9];
		for (int i = 0; i < 9; i++) {
			intArray[i] = Integer.parseInt(String. valueOf(state.charAt(i)));
		}
		int counter = 0;
		
		for (int i = 0; i < 9; i++) {
			if (intArray[i] != 0 && intArray[i] != i) 
			{
				int delta = Math.abs(i - intArray[i]);
				counter += (delta % 3 + delta / 3);
			}
		}
		return counter;
	}
	
	
	
	public int getDepth() {
		return depth;
	}

	public void setDepth(int depth) {
		this.depth = depth;
	}
	
	public void setHeuristic(int h)
	{
		heuristic = h;
	}

	public void increaseDepth()
	{
		depth+=1;
	}
	
	static int getInvCount(int[][] arr) 
	{ 
		int inv_count = 0; 
		for (int i = 0; i < 3 - 1; i++) 
			for (int j = i + 1; j < 3; j++) 
			
				// Value 0 is used for empty space 
				if (arr[j][i] > 0 && 
								arr[j][i] > arr[i][j]) 
					inv_count++; 
		return inv_count; 
	} 

	public boolean isSolvable() 
	{ 
		int val1 = Integer.parseInt(String.valueOf(state.charAt(0)));
		int val2 = Integer.parseInt(String.valueOf(state.charAt(1)));
		int val3 = Integer.parseInt(String.valueOf(state.charAt(2)));
		int val4 = Integer.parseInt(String.valueOf(state.charAt(3)));
		int val5 = Integer.parseInt(String.valueOf(state.charAt(4)));
		int val6 = Integer.parseInt(String.valueOf(state.charAt(5)));
		int val7 = Integer.parseInt(String.valueOf(state.charAt(6)));
		int val8 = Integer.parseInt(String.valueOf(state.charAt(7)));
		int val9 = Integer.parseInt(String.valueOf(state.charAt(8)));
		int[][] arr = { {val1, val2, val3}, {val4, val5, val6}, {val7, val8, val9}};
		int invCount = getInvCount(arr); 
		return (invCount % 2 == 0); 
	} 
	
	public String toString()
	{
//		String result = "";
//		for (int i = 0; i < 9; i++) {
//			result+=(state[i]+" ");
//			if (i == 2 || i == 5)
//				result+="\n";
//		}
//		result+="\n";
//		return result;
		String result = "";
		for (int i = 0; i < 9; i++)
		{
			result+=(state.charAt(i) + " ");
		}
		return result;
	}

	public boolean equals(Object o)  {
		Board c = (Board) o;
		if (c.getState() == this.getState())
		{
			return true;
		}
		else
			return false;
	}
	
	@Override
	public int compareTo(Board o) {
		if (heuristic == 1)
			return this.getMisplacedTiles() - o.getMisplacedTiles();
		else if (heuristic == 2)
			return this.getManhattanEval() - o.getManhattanEval();
		else
			return -1; // this means invalid heuristic
	}
}
