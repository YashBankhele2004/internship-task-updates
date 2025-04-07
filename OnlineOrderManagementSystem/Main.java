import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        OrderDAO orderDAO = new OrderDAO();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add Order");
            System.out.println("2. View Orders");
            System.out.println("3. Delete Order");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter product name: ");   
                    String productName = scanner.nextLine();
                    System.out.print("Enter quantity: ");
                    int quantity = scanner.nextInt();
                    System.out.print("Enter price: ");
                    double price = scanner.nextDouble();
                    orderDAO.addOrder(productName, quantity, price);
                    break;

                case 2:
                    List<String> orders = orderDAO.getAllOrders();
                    if (orders.isEmpty()) {
                        System.out.println("No orders found.");
                    } else {
                        orders.forEach(System.out::println);
                    }
                    break;

                case 3:
                    System.out.print("Enter order ID to delete: ");
                    int orderId = scanner.nextInt();
                    orderDAO.deleteOrder(orderId);
                    break;

                case 4:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;

                default:
                    System.out.println("Invalid choice. Try again.");
            }
        }
    }
}
