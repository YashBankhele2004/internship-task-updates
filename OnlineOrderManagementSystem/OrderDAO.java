import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class OrderDAO {
    
    // Insert Order
    public void addOrder(String productName, int quantity, double price) {
        String sql = "INSERT INTO orders (product_name, quantity, price) VALUES (?, ?, ?)";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
             
            stmt.setString(1, productName);
            stmt.setInt(2, quantity);
            stmt.setDouble(3, price);
            stmt.executeUpdate();
            System.out.println("Order added successfully!");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Retrieve All Orders
    public List<String> getAllOrders() {
        List<String> orders = new ArrayList<>();
        String sql = "SELECT * FROM orders";
        try (Connection conn = DatabaseConnection.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
             
            while (rs.next()) {
                orders.add("ID: " + rs.getInt("id") + 
                           ", Product: " + rs.getString("product_name") + 
                           ", Quantity: " + rs.getInt("quantity") + 
                           ", Price: " + rs.getDouble("price") + 
                           ", Date: " + rs.getTimestamp("order_date"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return orders;
    }

    // Delete Order
    public void deleteOrder(int orderId) {
        String sql = "DELETE FROM orders WHERE id = ?";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
             
            stmt.setInt(1, orderId);
            int rowsAffected = stmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Order deleted successfully!");
            } else {
                System.out.println("Order not found!");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
