<?php

include('connect.php');

$name = $_POST['name'];
$email = $_POST['email'];
$state = $_POST['state'];
$license_plate = $_POST['license_plate'];
$type = $_POST['type'];
$member_start_date = $_POST['start_date'];
$member_end_date = $_POST['end_date'];
$renew = $_POST['renew'];

$query = "INSERT INTO subscription (name, subscription_type, subscription_date, subscription_expired, renew, license_plate, state, email) VALUES ('$name', '$type', '$member_start_date', '$member_end_date', '$renew', '$license_plate', '$state', '$email')"; 

if(!mysqli_query($CONNECT, $query)) {
echo mysqli_error($CONNECT);
}

header("Location: user.php");

# Maybe the single quotes? '$name' --> $name   ?
//hold on

?>