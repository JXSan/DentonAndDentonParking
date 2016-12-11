<?php
// Session Started
SESSION_START();

// Includes
include('connect.php');

# Check if username is in the database
$check = $_SESSION['username'];
$query = ("SELECT * FROM user WHERE username = '$check'");
$result = mysqli_fetch_assoc((mysqli_query($CONNECT, $query)));

$first_name = $result['first_name'];
$last_name = $result['last_name'];

# Tickets Issued Today Query
$sql = "SELECT * FROM ticket LIMIT 0,20";
$r = $CONNECT->query($sql);

# Subscribers Query
$sql_subscribers = "SELECT * FROM subscription LIMIT 0,20";
$r_subscribers = $CONNECT->query($sql_subscribers);

$append = "";
$subscribers = "";


# Create variables for statistics

# -- TODAYS REVENUE -- #

$query_todays_revenue = ("SELECT SUM(cost) FROM ticket WHERE date = CURDATE()");
$result_todays_revenue = mysqli_fetch_assoc((mysqli_query($CONNECT, $query_todays_revenue)));

$todays_revenue = $result_todays_revenue['SUM(cost)'];

# -- TICKETS ISSUED TODAY -- #

$query_tickets_issued = ("SELECT COUNT(ticket_id) FROM ticket");
$result_tickets_issued = mysqli_fetch_assoc((mysqli_query($CONNECT, $query_tickets_issued)));

$tickets_issued = $result_tickets_issued['COUNT(ticket_id)'];

# -- TOTAL SUBSCRIBERS -- #

$query_total_subscribers = ("SELECT COUNT(membership_id) FROM subscription");
$result_total_subscribers = mysqli_fetch_assoc((mysqli_query($CONNECT, $query_total_subscribers)));

$total_subscribers = $result_total_subscribers['COUNT(membership_id)'];

# -- TOTAL SALES -- #

$query_total_sales = ("SELECT SUM(cost) FROM ticket");
$result_total_sales = mysqli_fetch_assoc((mysqli_query($CONNECT, $query_total_sales)));

$total_sales = $result_total_sales['SUM(cost)'];

# -- TOTAL SALES for DECEMBER -- #

$query_total_sales_monthly = ("SELECT SUM(cost) FROM ticket WHERE MONTH(date) = 12");
$result_total_sales_monthly = mysqli_fetch_assoc((mysqli_query($CONNECT, $query_total_sales_monthly)));

$total_sales_monthly = $result_total_sales_monthly['SUM(cost)'];

# -- ------------------- -- #

# Print Tickets Issues Today Table
if ($r->num_rows > 0) {
    while($row = $r->fetch_assoc()) {
        $append .="<tr><td>".$row["ticket_id"]."</td><td>".$row["time"]."</td>
                                            <td>".$row["time_out"]."</td>
                                            <td>".$row["date"]."</td>
                                            <td>$".$row["cost"]."</td>
                                        </tr>";
    }
}

# Print Subscribers Table
if ($r_subscribers->num_rows > 0) {
    while($row = $r_subscribers->fetch_assoc()) {
        $subscribers .="<tr><td>".$row["membership_id"]."</td><td>".$row["name"]."</td>
                                            <td>".$row["email"]."</td>
                                            <td>".$row["subscription_type"]."</td>
                                            <td>".$row["subscription_date"]."</td>
                                            <td>".$row["subscription_expired"]."</td>
                                            <td>".$row["license_plate"]."</td>
                                            <td>".$row["state"]."</td>
                                            <td>".$row["renew"]."</td>
                                            <td>$".$row["cost"]."</td>
                                        </tr>";
    }
}

/*

*/

?>