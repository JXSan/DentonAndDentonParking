<?php
SESSION_START();
$mysqli = new mysqli("138.197.34.187", "nyit", "nyit123", "denton");

if($result = $mysqli->query("SELECT * FROM ticket")){
    if($count = $result->num_rows){
    while($row = $result->fetch_object()){
        echo $row['ticket_id'];
    }
    }
}
?>