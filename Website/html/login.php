<?php

SESSION_START();

#include('index.php');
include('connect.php');

# If the form is not submitted
if(!isset($_POST['submit'])){
    //echo 'Please log in to continue';
    die(" <a href='index.php'> Log In </a> ");
}

# Assigning variables
$username = $_POST['username'];
$passwordAttempt = $_POST['password'];
$name = ("SELECT first_name FROM user WHERE username = '$username'");

# Include connect
include('connect.php');

# Check if username is in the database
$query = ("SELECT * FROM user WHERE username = '$username'");
$result = mysqli_query($CONNECT, $query);
$hits = mysqli_affected_rows($CONNECT);

if($hits < 1){
    header("Location: index.php");
}

while($row = mysqli_fetch_assoc($result)){
    $db_password = $row['password'];
    
    if($db_password != $passwordAttempt){
        header("Location: index.php");
    }
    else{
        // User has successfully logged in.        
        // Begin session.
        $_SESSION['username'] = $username;
        echo $_SESSION['username'];
        #header("Location: logged_in.php");
        header("Location: dashboard.php");
    }
}

?>
