package DASAR;

public class User {
    private String name;
    private String email;
    private String noHP;

    public User(String name, String email, String noHP) {
        this.name = name;
        this.email = email;
        this.noHP = noHP;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public String getNoHP() {
        return noHP;
    }
}