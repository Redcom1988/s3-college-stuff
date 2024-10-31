package DASAR;

public class Admin extends User {
    private String username;

    public Admin(String name, String email, String noHP, String username) {
        super(name, email, noHP);
        this.username = username;
    }

    public String getUsername() {
        return username;
    }

    public static void main(String[] args) {
        Admin newAdmin = new Admin("Nanda", "nanda@gmail.com", "081234567890", "NandTheMan");
        System.out.println(newAdmin.getName());
    }
}
