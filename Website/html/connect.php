<?php
//======================== CONNECTION VARIABLE START HERE ========================\\
$DB_HOST = "138.197.34.187";
$DB_USERNAME = "nyit";
$DB_PASSWORD = "nyit123";
$DB_NAME = "denton";

//======================== START CONNECTION ========================\\
$CONNECT = mysqli_connect($DB_HOST, $DB_USERNAME, $DB_PASSWORD, $DB_NAME) or die ("Could not connect to database.");
    

?>