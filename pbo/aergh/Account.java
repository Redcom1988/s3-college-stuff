package DASAR;
import java.util.*;

public class Account {
    private List<User> list;

    public Account() {
        this.list = new ArrayList<>();
    }

    public void getList() {
        System.out.println("List Akun\n");
        if (list.isEmpty()) {
            System.out.println("Tidak ada akun yang terdaftar.");
        } else {
            for (User user : list) {
                System.out.println("Nama : " + user.getName());
                System.out.println("Email : " + user.getEmail());
                System.out.println("No HP : " + user.getNoHP());
                System.out.println();
            }
        }
    }

    public void addList(User user) {
        list.add(user);
    }

    public void regist(String name, String email, String noHP) {
        User newUser = new User(name, email, noHP);
        addList(newUser);
    }

    public boolean delete(String name) {
        Iterator<User> iterator = list.iterator();
        while (iterator.hasNext()) {
            User user = iterator.next();
            if (user.getName().equals(name)) {
                iterator.remove();
                return true;
            }
        }
        return false;
    }
}