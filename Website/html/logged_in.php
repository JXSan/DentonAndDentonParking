<?php

SESSION_START();

if(!isset($_SESSION['username'])){
   // echo 'Please log in to continue';
    die(" <a href='index.php'> Log In </a> ");
}

$username = $_SESSION['username'];

?>