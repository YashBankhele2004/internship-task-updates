<%@ page import="java.util.List" %>
<%@ page import="Order" %>
<%@ page contentType="text/html; charset=UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <title>Online Order Management</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid black; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        form { margin-top: 20px; }
    </style>
</head>
<body>

    <h2>Place an Order</h2>
    <form action="OrderServlet" method="post">
        <input type="hidden" name="action" value="add">
        <label>Product Name: <input type="text" name="product_name" required></label><br><br>
        <label>Quantity: <input type="number" name="quantity" required></label><br><br>
        <label>Price: <input type="number" step="0.01" name="price" required></label><br><br>
        <button type="submit">Submit Order</button>
    </form>

    <h2>Order History</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Product Name</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>Order Date</th>
            <th>Action</th>
        </tr>
        <%
            List<Order> orders = (List<Order>) request.getAttribute("orders");
            if (orders != null) {
                for (Order order : orders) {
        %>
        <tr>
            <td><%= order.getId() %></td>
            <td><%= order.getProductName() %></td>
            <td><%= order.getQuantity() %></td>
            <td><%= order.getPrice() %></td>
            <td><%= order.getOrderDate() %></td>
            <td>
                <form action="OrderServlet" method="post" style="display:inline;">
                    <input type="hidden" name="action" value="delete">
                    <input type="hidden" name="order_id" value="<%= order.getId() %>">
                    <button type="submit">Delete</button>
                </form>
            </td>
        </tr>
        <% } } %>
    </table>

</body>
</html>
