public class Book {
    // Private fields
    private String title;
    private String author;
    private String publisher;
    private int pages;

    // Constructor to initialize the book details
    public Book(String title, String author, String publisher, int pages) {
        this.title = title;
        this.author = author;
        this.publisher = publisher;
        this.pages = pages;
    }

    // Non-void method to get book details
    public String getBookInfo() {
        return "Title: " + title + ", Author: " + author + ", Publisher: " + publisher + ", Pages: " + pages;
    }

    // Non-void method to estimate reading time
    public double estimateReadingTime(double readingSpeed) {
        if (readingSpeed <= 0) {
            throw new IllegalArgumentException("Reading speed must be greater than 0.");
        }
        // Estimate time in hours to finish the book
        double estimatedTime = pages / readingSpeed;
        return estimatedTime;
    }

    public static void main(String[] args) {
        // Creating instances (objects) of the Book class
        Book book1 = new Book("1984", "George Orwell", "Secker & Warburg", 328);
        Book book2 = new Book("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons", 180);

        // Calling non-void methods and printing the results
        System.out.println(book1.getBookInfo()); // Outputs details of book1
        System.out.println("Estimated reading time: " + book1.estimateReadingTime(50) + " hours"); // Assumes reading
                                                                                                   // speed of 50 pages
                                                                                                   // per hour

        System.out.println(book2.getBookInfo()); // Outputs details of book2
        System.out.println("Estimated reading time: " + book2.estimateReadingTime(75) + " hours"); // Assumes reading
                                                                                                   // speed of 75 pages
                                                                                                   // per hour
    }
}
