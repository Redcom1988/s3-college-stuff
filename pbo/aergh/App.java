package DASAR;
import java.util.*;
import LANJUTAN.*;

public class App {
    public static void main(String[] args) {
        Account account = new Account();
        Scanner sc = new Scanner(System.in);
        System.out.println("== CRUD Akun Dasar ==");

        while (true) {
            System.out.println("\nPilih Menu : ");
            System.out.println("1. Buat Akun\n2. Lihat Data\n3. Hapus Data\n4. Keluar\n");
            System.out.print("Pilih : ");
            int choice = sc.nextInt();
            sc.nextLine();
            
            switch (choice) {
                case 1:
                    System.out.print("Nama : ");
                    String name = sc.nextLine();
                    System.out.print("Email : ");
                    String email = sc.nextLine();
                    System.out.print("No HP : ");
                    String noHP = sc.nextLine();
                    account.regist(name, email, noHP);
                    System.out.println("Berhasil Buat Akun");
                    break;
                case 2:
                    account.getList();
                    break;
                case 3:
                    System.out.print("Masukkan nama yang ingin dihapus : ");
                    String nama = sc.nextLine();
                    Boolean yes = account.delete(nama);
                    if(yes) System.out.println("Data berhasil dihapus");
                    else System.out.println("Data gagal dihapus");
                    break;
                case 4:
                    System.out.println("Terima kasih telah menggunakan aplikasi ini.");
                    sc.close();
                    System.exit(0);
                default:
                    System.out.println("Pilihan tidak valid. Silakan coba lagi.");
                    break;
            }
        }
    }
}