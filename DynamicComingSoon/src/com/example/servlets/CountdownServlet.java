package com.example.servlets;

import db.DBConnection;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/countdown")
public class CountdownServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String launchDate = "";
        String message = "";

        try (Connection conn = DBConnection.getConnection()) {
            String query = "SELECT launch_date, message FROM countdown ORDER BY id DESC LIMIT 1";
            PreparedStatement stmt = conn.prepareStatement(query);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                launchDate = rs.getString("launch_date");
                message = rs.getString("message");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        request.setAttribute("launchDate", launchDate);
        request.setAttribute("message", message);
        request.getRequestDispatcher("comingsoon.jsp").forward(request, response);
    }
}
