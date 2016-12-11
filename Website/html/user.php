<?php

SESSION_START();

if(!isset($_SESSION['username'])){
   // echo 'Please log in to continue';
    die(" <a href='index.php'> Log In </a> ");
}

$username = $_SESSION['username'];

include('connect.php');
include('load.php');
?>

<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<link rel="icon" type="image/png" href="assets/img/favicon.ico">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

	<title>Denton Parking Admin Portal</title>

	<meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />
    <meta name="viewport" content="width=device-width" />


    <!-- Bootstrap core CSS     -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Animation library for notifications   -->
    <link href="assets/css/animate.min.css" rel="stylesheet"/>

    <!--  Light Bootstrap Table core CSS    -->
    <link href="assets/css/light-bootstrap-dashboard.css" rel="stylesheet"/>


    <!--  CSS for Demo Purpose, don't include it in your project     -->
    <link href="assets/css/demo.css" rel="stylesheet" />


    <!--     Fonts and icons     -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300' rel='stylesheet' type='text/css'>
    <link href="assets/css/pe-icon-7-stroke.css" rel="stylesheet" />
</head>
<body>

<div class="wrapper">
    <div class="sidebar" data-color="purple" data-image="assets/img/sidebar-5.jpg">

    <!--   you can change the color of the sidebar using: data-color="blue | azure | green | orange | red | purple" -->


    	<div class="sidebar-wrapper">
            <div class="logo">
                <a href="dashboard.php" class="simple-text">
                    Denton Parking
                </a>
            </div>

            <ul class="nav">
                <li class="active">
                    <a href="dashboard.php">
                        <i class="pe-7s-graph"></i>
                        <p>Dashboard</p>
                    </a>
                </li>
                <li>
                    <a href="user.php">
                        <i class="pe-7s-user"></i>
                        <p>Subscriber Sign Up</p>
                    </a>
                </li>
                <li>
                    <a href="subscribers.php">
                        <i class="pe-7s-note2"></i>
                        <p>Subscribers</p>
                    </a>
                </li>
            </ul>
    	</div>
    </div>

    <div class="main-panel">
        <nav class="navbar navbar-default navbar-fixed">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navigation-example-2">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#"><?php echo 'Welcome, '.$first_name ?></a>
                </div>
                <div class="collapse navbar-collapse">
                    <ul class="nav navbar-nav navbar-left">
                        <li>
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-dashboard"></i>
                            </a>
                        </li>
                        <li>
                           <a href="">
                                <i class="fa fa-search"></i>
                            </a>
                        </li>
                    </ul>

                    <ul class="nav navbar-nav navbar-right">
                        <li>
                            <a href="index.php">
                                Log out
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>


        <div class="content">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-8">
                        <div class="card">
                            <div class="header">
                                <h4 class="title">Subscriber Sign Up Form - Enter Information</h4>
                            </div>
                            <div class="content">
                                <form action="subscriber_signup_form.php" method="POST">
                                    <div class="row">
                                        <div class="col-md-5">
                                            <div class="form-group">
                                                <label>Name</label>
                                                <input type="text" name = "name" class="form-control" placeholder="John Doe" value="">
                                            </div>
                                        </div>
                                        <div class="col-md-4">
                                            <div class="form-group">
                                                <label for="exampleInputEmail1">Email address</label>
                                                <input type="email" name = "email" class="form-control" placeholder="Email" value="">
                                            </div>
                                        </div>
                                    </div>
                                    
                                        

                                    <div class="row">
                                        <div class="col-md-12">
                                            <div class="form-group">
                                                <label>Address</label>
                                                <input type="text" name = "address" class="form-control" placeholder="Home Address" value="">
                                            </div>
                                        </div>
                                    </div>

                                    <div class="row">
                                        <div class="col-md-4">
                                            <div class="form-group">
                                                <label>City</label>
                                                <input type="text" name = "city" class="form-control" placeholder="City" value="">
                                            </div>
                                        </div>
                                        <div class="col-md-3">
                                            <div class="form-group">
                                                <label>State</label>
                                                <select name="state">
                                                    <option  value="AL">Alabama</option>
                                                    <option  value="AK">Alaska</option>
                                                    <option  value="AZ">Arizona</option>
                                                    <option  value="AR">Arkansas</option>
                                                    <option  value="CA">California</option>
                                                    <option  value="CO">Colorado</option>
                                                    <option  value="CT">Connecticut</option>
                                                    <option  value="DE">Delaware</option>
                                                    <option  value="DC">District Of Columbia</option>
                                                    <option  value="FL">Florida</option>
                                                    <option  value="GA">Georgia</option>
                                                    <option  value="HI">Hawaii</option>
                                                    <option  value="ID">Idaho</option>
                                                    <option  value="IL">Illinois</option>
                                                    <option  value="IN">Indiana</option>
                                                    <option  value="IA">Iowa</option>
                                                    <option  value="KS">Kansas</option>
                                                    <option  value="KY">Kentucky</option>
                                                    <option  value="LA">Louisiana</option>
                                                    <option  value="ME">Maine</option>
                                                    <option  value="MD">Maryland</option>
                                                    <option  value="MA">Massachusetts</option>
                                                    <option  value="MI">Michigan</option>
                                                    <option  value="MN">Minnesota</option>
                                                    <option  value="MS">Mississippi</option>
                                                    <option  value="MO">Missouri</option>
                                                    <option  value="MT">Montana</option>
                                                    <option  value="NE">Nebraska</option>
                                                    <option  value="NV">Nevada</option>
                                                    <option  value="NH">New Hampshire</option>
                                                    <option  value="NJ">New Jersey</option>
                                                    <option  value="NM">New Mexico</option>
                                                    <option  value="NY">New York</option>
                                                    <option  value="NC">North Carolina</option>
                                                    <option  value="ND">North Dakota</option>
                                                    <option  value="OH">Ohio</option>
                                                    <option  value="OK">Oklahoma</option>
                                                    <option  value="OR">Oregon</option>
                                                    <option  value="PA">Pennsylvania</option>
                                                    <option  value="RI">Rhode Island</option>
                                                    <option  value="SC">South Carolina</option>
                                                    <option  value="SD">South Dakota</option>
                                                    <option  value="TN">Tennessee</option>
                                                    <option  value="TX">Texas</option>
                                                    <option  value="UT">Utah</option>
                                                    <option  value="VT">Vermont</option>
                                                    <option  value="VA">Virginia</option>
                                                    <option  value="WA">Washington</option>
                                                    <option  value="WV">West Virginia</option>
                                                    <option  value="WI">Wisconsin</option>
                                                    <option  value="WY">Wyoming</option>
                                                </select>
                                            </div>
                                        </div>
    
                                        <div class="col-md-4">
                                            <div class="form-group">
                                                <label>Postal Code</label>
                                                <input type="number" name = "postal" class="form-control" placeholder="ZIP Code">
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="row">
                                        <div class="col-md-12">
                                            <div class="form-group">
                                                <label>License Plate Number</label>
                                                <input type="text" name = "license_plate" class="form-control" placeholder="KRH457" value="">
                                            </div>
                                        </div>
                                    </div>
                                    
                                        <div class="col-md-3">
                                            <div class="form-group">
                                                <label>Type</label>
                                                <select name="type">
                                                    <option value="D">Daily</option>
                                                    <option  value="M">Monthly</option>
                                                    <option  value="A">Annualy</option>
                                                </select>
                                            </div>
                                        </div>
                                    
                                    <div class="col-md-4">
                                            <div class="form-group">
                                                <label for="meeting">Membership Start Date:</label><input name = "start_date" id="meeting" type="date" value=""/>
                                            </div>
                                        </div>
                                    
                                    <div class="col-md-4">
                                            <div class="form-group">
                                                <label for="meeting">Membership End Date:</label><input name = "end_date" id="meeting" type="date" value=""/>
                                            </div>
                                        </div>
                                    
                                    
                                    <div class="col-md-3">
                                            <div class="form-group">
                                                <label>Renew</label>
                                                <select name="renew">
                                                    <option value="Y">Yes</option>
                                                    <option  value="N">No</option>
                                                </select>
                                            </div>
                                        </div>

                                    <button type="submit" class="btn btn-info btn-fill pull-right">Submit</button>
                                    <div class="clearfix"></div>
                                </form>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>


        <footer class="footer">
            <div class="container-fluid">
                <nav class="pull-left">
                    <ul>
                        <li>
                            <a href="#">
                                Home
                            </a>
                        </li>
                        <li>
                            <a href="company.html">
                                Company
                            </a>
                        </li>
                    </ul>
                </nav>
                <p class="copyright pull-right">
                    &copy; 2016 Denton Parking Project 3
                </p>
            </div>
        </footer>

    </div>
</div>


</body>

    <!--   Core JS Files   -->
    <script src="assets/js/jquery-1.10.2.js" type="text/javascript"></script>
	<script src="assets/js/bootstrap.min.js" type="text/javascript"></script>

	<!--  Checkbox, Radio & Switch Plugins -->
	<script src="assets/js/bootstrap-checkbox-radio-switch.js"></script>

	<!--  Charts Plugin -->
	<script src="assets/js/chartist.min.js"></script>

    <!--  Notifications Plugin    -->
    <script src="assets/js/bootstrap-notify.js"></script>

    <!--  Google Maps Plugin    -->
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>

    <!-- Light Bootstrap Table Core javascript and methods for Demo purpose -->
	<script src="assets/js/light-bootstrap-dashboard.js"></script>

	<!-- Light Bootstrap Table DEMO methods, don't include it in your project! -->
	<script src="assets/js/demo.js"></script>

</html>
