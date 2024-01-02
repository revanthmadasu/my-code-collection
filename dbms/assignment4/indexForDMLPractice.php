<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "universitydb";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
else{	
	echo "Successfully connected";
} 

// perform some data manipulation
// insert a row in department table

$sql = "insert into department values ('Physics', 'Business', 99999.00)";
if ($conn->query($sql) === TRUE) {
	echo "<br/>"; // new line
    echo "Insertion successful";
} else {
	echo "<br/>"; // new line 
    echo "Error accessing database: " . $conn->error;
}


// Practice 1-- insert a new department Law--Morril--10000
// Practice 2---insert a row in student table

// Test 3---update: increase the budget of Physics department by 5 percent

$sql = "update department set budget = budget*1.05 where dept_name = 'Physics'";
if ($conn->query($sql) === TRUE) {
	echo "<br/>"; // new line
    echo "Update successful";
} else {
	echo "<br/>"; // new line 
    echo "Error accessing database: " . $conn->error;
}


// Select command
$sql = "SELECT * FROM department";
$result = $conn->query($sql);

//number of rows
echo "<br/>Total records: $result->num_rows<br/>";

//display the records
if ($result->num_rows > 0) {	
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "dept name: " . $row["dept_name"]. " - building: " . $row["building"]. " " . $row["budget"]. "<br>";
    }
} else {
    echo "0 results";
}


// Test 4--show the budget of CSC department
$sql = "select budget from department where dept_name = 'biology'";
$result = $conn->query($sql);
echo "<br/>Total records: $result->num_rows<br/>";
$values = $result->fetch_assoc();
echo $values["budget"];

//terminate connection
$conn->close();
?>