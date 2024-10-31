import java.util.*;

public class Buku {

    // atribut buku
    private String judulBuku = "";
    private String kategori = "";
    private String penulis = "";
    private String jenisBuku = "";

    // berbagai overload konstruktor buku
    public Buku(String judulBuku) {
        this.judulBuku = judulBuku;
        this.kategori = "Tidak Ada";
        this.penulis = "Tidak Ada";
        this.jenisBuku = "Buku ATK/Perlengkapan";
    }
    public Buku(String judulBuku, String kategori) {
        this.judulBuku = judulBuku;
        this.kategori = kategori;
        this.penulis = "Tidak Ada";
        this.jenisBuku = "Buku Tanpa Penulis";
    }
    public Buku(String judulBuku, String kategori, String penulis) {
        this.judulBuku = judulBuku;
        this.kategori = kategori;
        this.penulis = penulis;
        this.jenisBuku = "Buku Dengan Penulis";
    }

    // getter method
    public String getJudulBuku() { return judulBuku; }
    public String getKategori() { return kategori; }
    public String getPenulis() { return penulis; }
    public String getJenisBuku() { return jenisBuku; }

    // method dengan parameter objek buku
    boolean judulSama(Buku lain) {
        return this.judulBuku.equals(lain.judulBuku);
    }
    boolean adaKategori(Buku lain) {
        if (lain.kategori.length() > 0)
            return true;
        return false;
    }
    boolean adaPenulis(Buku lain) {
        if (lain.penulis.length() > 0)
            return true;
        return false;
    }

    public static void clearScreen() {
        try {
            // Menggunakan ANSI escape code
            System.out.print("\033[H\033[2J");
            System.out.flush();

            // Menggunakan Runtime untuk eksekusi perintah sistem
            if (System.getProperty("os.name").contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            }
        } catch (Exception e) {
            // Jika semua metode di atas gagal, gunakan cara sederhana
            for (int i = 0; i < 50; ++i)
                System.out.println();
        }
    }

    public static void main(String[] args) {

        // deklarasi variabel
        List<Buku> daftarBuku = new ArrayList<>();
        Scanner sc = new Scanner(System.in);

        while (true) {
            // menu pilihan
            clearScreen();
            System.out.println("Program Toko Buku");
            System.out.println("1. Tambah Buku");
            System.out.println("2. Cek Buku");
            System.out.println("3. Edit Info Buku");
            System.out.println("4. Hapus Info Buku");
            System.out.println("5. Keluar");

            // input user
            System.out.print("\nPilihan : ");
            int pilihan = sc.nextInt();
            sc.nextLine();

            switch (pilihan) {
                case 1:
                    // input judul buku
                    System.out.println("\nMasukkan data buku:");
                    System.out.print("Judul Buku    : ");
                    String judulLengkap = sc.nextLine();

                    // cek untuk judul yang sama
                    boolean duplikat = false;
                    for (Buku bukuAda : daftarBuku) {
                        if (bukuAda.judulSama(new Buku(judulLengkap))) {
                            duplikat = true;
                            break;
                        }
                    }
                    if (duplikat) {
                        System.out.println("\nBuku dengan judul yang sama sudah ada!");
                        break;
                    }

                    // input kategori buku (opsional)
                    System.out.print("Kategori Buku : ");
                    String kategoriLengkap = sc.nextLine();

                    // input penulis buku (opsional)
                    System.out.print("Penulis Buku  : ");
                    String penulisLengkap = sc.nextLine();

                    // handle case untuk konstruktor
                    Buku bukuBaru;
                    if (!penulisLengkap.isEmpty() && !kategoriLengkap.isEmpty()) {
                        bukuBaru = new Buku(judulLengkap, kategoriLengkap, penulisLengkap); // data lengkap
                    } else if (!kategoriLengkap.isEmpty()) {
                        bukuBaru = new Buku(judulLengkap, kategoriLengkap); // judul dan kategori
                    } else {
                        bukuBaru = new Buku(judulLengkap); // judul saja
                    }

                    // tambah buku ke daftar
                    daftarBuku.add(bukuBaru);
                    System.out.println("\nBuku " + bukuBaru.getJudulBuku() + " berhasil ditambahkan!");
                    break;

                case 2:
                    // input judul buku
                    System.out.print("Masukkan judul buku yang ingin dicek : ");
                    String judulCari = sc.nextLine();
                    boolean bukuDitemukan = false;

                    // tampilkan informasi buku
                    for (Buku buku : daftarBuku) {
                        if (buku.getJudulBuku().equalsIgnoreCase(judulCari)) {
                            System.out.println("\nInformasi Buku:");
                            System.out.println("Judul Buku    : " + buku.getJudulBuku());
                            System.out.println("Kategori Buku : " + buku.getKategori());
                            System.out.println("Penulis Buku  : " + buku.getPenulis());
                            System.out.println("Jenis Buku    : " + buku.getJenisBuku());
                            bukuDitemukan = true;
                            break;
                        }
                    }
                    if (!bukuDitemukan) {
                        System.out.println("Buku " + judulCari + " tidak ditemukan.");
                    }
                    break;

                case 3:
                    System.out.print("Masukkan judul buku yang ingin diedit : ");
                    String judulEdit = sc.nextLine();
                    bukuDitemukan = false;

                    for (int i = 0; i < daftarBuku.size(); i++) {
                        if (daftarBuku.get(i).getJudulBuku().equalsIgnoreCase(judulEdit)) {
                            Buku bukuLama = daftarBuku.get(i);

                            // Tampilkan informasi buku yang akan diedit
                            System.out.println("\nInformasi Buku Saat Ini:");
                            System.out.println("Judul Buku    : " + bukuLama.getJudulBuku());
                            System.out.println("Kategori Buku : " + bukuLama.getKategori());
                            System.out.println("Penulis Buku  : " + bukuLama.getPenulis());
                            System.out.println("Jenis Buku    : " + bukuLama.getJenisBuku());

                            // pilih jenis buku baru
                            System.out.println("\nJenis Buku Baru:");
                            System.out.println("1. Buku Dengan Penulis");
                            System.out.println("2. Buku Tanpa Penulis");
                            System.out.println("3. Buku ATK/Perlengkapan");
                            System.out.print("Pilih jenis buku baru (1-3): ");
                            int jenisBukuBaru = sc.nextInt();
                            sc.nextLine();

                            // update data buku
                            Buku bukuUpdate;
                            switch (jenisBukuBaru) {
                                case 1:
                                    System.out.print("Judul Buku baru    : ");
                                    String judulBaru = sc.nextLine();
                                    System.out.print("Kategori Buku baru : ");
                                    String kategoriBaru = sc.nextLine();
                                    System.out.print("Penulis Buku baru  : ");
                                    String penulisBaru = sc.nextLine();
                                    bukuUpdate = new Buku(judulBaru, kategoriBaru, penulisBaru);
                                    break;

                                case 2:
                                    System.out.print("Judul Buku baru    : ");
                                    judulBaru = sc.nextLine();
                                    System.out.print("Kategori Buku baru : ");
                                    kategoriBaru = sc.nextLine();
                                    bukuUpdate = new Buku(judulBaru, kategoriBaru);
                                    break;

                                case 3:
                                    System.out.print("Judul Buku baru : ");
                                    judulBaru = sc.nextLine();
                                    bukuUpdate = new Buku(judulBaru);
                                    break;

                                default:
                                    System.out.println("Jenis buku tidak valid!");
                                    return;
                            }

                            // update buku pada daftar
                            daftarBuku.set(i, bukuUpdate);
                            System.out.println("Buku berhasil diupdate!");
                            bukuDitemukan = true;
                            break;
                        }
                    }

                    if (!bukuDitemukan) {
                        System.out.println("Buku " + judulEdit + " tidak ditemukan.");
                    }
                    break;

                case 4:
                    // input judul buku
                    System.out.print("Masukkan judul buku yang ingin dihapus : ");
                    String judulHapus = sc.nextLine();
                    bukuDitemukan = false;

                    for (int i = 0; i < daftarBuku.size(); i++) {
                        if (daftarBuku.get(i).getJudulBuku().equalsIgnoreCase(judulHapus)) {
                            Buku buku = daftarBuku.get(i);

                            // tampilkan informasi buku yang akan dihapus
                            System.out.println("\nInformasi Buku yang akan dihapus:");
                            System.out.println("Judul Buku    : " + buku.getJudulBuku());
                            System.out.println("Kategori Buku : " + buku.getKategori());
                            System.out.println("Penulis Buku  : " + buku.getPenulis());
                            System.out.println("Jenis Buku    : " + buku.getJenisBuku());

                            // konfirmasi penghapusan
                            System.out.print("\nApakah Anda yakin ingin menghapus buku ini? (Y/N) : ");
                            String konfirmasi = sc.nextLine().toUpperCase();

                            if (konfirmasi.equals("Y")) {
                                daftarBuku.remove(i);
                                System.out.println("Buku berhasil dihapus!");
                            } else {
                                System.out.println("Penghapusan dibatalkan.");
                            }

                            bukuDitemukan = true;
                            break;
                        }
                    }

                    if (!bukuDitemukan) {
                        System.out.println("Buku " + judulHapus + " tidak ditemukan.");
                    }
                    break;

                case 5:
                    System.out.println("Terima kasih.");
                    sc.close();
                    System.exit(0);

                default:
                    System.out.println("Pilihan tidak tersedia.");
                    break;
            }

            System.out.println("\nTekan Enter untuk melanjutkan...");
            sc.nextLine();
        }
    }
}