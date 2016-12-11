<?php
// Session Started
SESSION_START();

// Includes
include('connect.php');

/*
THIS SECTION DOES ALL THE CALCULATIONS TO BE DISPLAYED IN THE DASHBOARD
*/
$query = ("SELECT SUM(cost) FROM ticket;");
$result = mysqli_fetch_assoc((mysqli_query($CONNECT, $query)));

$sum = $result['SUM(cost)'];
echo $sum;

?>