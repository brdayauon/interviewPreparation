
public class Node implements Comparable<Node>
{
	private Board board;
	private int depth;
	
	public Node(Board board, int depth)
	{
		this.board = board;
		this.depth = depth;
	}

	public Board getBoard() {
		return board;
	}

	public void setBoard(Board board) {
		this.board = board;
	}

	public int getDepth() {
		return depth;
	}

	public void setDepth(int depth) {
		this.depth = depth;
	}
	
	public int compareTo(Node o) {
		return this.getBoard().compareTo(o.getBoard()) + (this.getDepth() - o.getDepth());
	}
}
