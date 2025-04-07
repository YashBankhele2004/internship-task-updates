import java.sql.Timestamp;

public class Order {
    private int id;
    private String productName;
    private int quantity;
    private double price;
    private Timestamp orderDate;

    public Order(int id, String productName, int quantity, double price, Timestamp orderDate) {
        this.id = id;
        this.productName = productName;
        this.quantity = quantity;
        this.price = price;
        this.orderDate = orderDate;
    }

    public int getId() { return id; }
    public String getProductName() { return productName; }
    public int getQuantity() { return quantity; }
    public double getPrice() { return price; }
    public Timestamp getOrderDate() { return orderDate; }
}
