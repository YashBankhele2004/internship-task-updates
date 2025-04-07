<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coming Soon</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <script>
        const launchDate = new Date('<%= request.getAttribute("launchDate") %>').getTime();

        function updateCountdown() {
            const now = new Date().getTime();
            const distance = launchDate - now;

            if (distance < 0) {
                document.getElementById("timer").innerHTML = "Launched!";
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            document.getElementById("timer").innerHTML =
                `${days}d ${hours}h ${minutes}m ${seconds}s`;
        }

        setInterval(updateCountdown, 1000);
    </script>
</head>
<body class="bg-dark text-light text-center">
    <div class="container">
        <h1 class="mt-5"><%= request.getAttribute("message") %></h1>
        <h2 id="timer" class="my-4"></h2>
        <p>Stay tuned for our launch!</p>
    </div>
</body>
</html>