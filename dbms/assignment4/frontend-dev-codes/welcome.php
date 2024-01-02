<html>
<body>

<?php
$value1 = $_POST["dept_name"];
$value2 = $_POST["building"];
$value3 = $_POST["budget"];
echo $value1;
echo "  ";
echo $value2;
echo " ";
echo $value3;

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
	echo "<br/>connected to database successfully<br/>";
}

$sql = "insert into department (dept_name, building, budget) values ('$value1', '$value2', '$value3')";
if ($conn->query($sql) === TRUE) {
    echo "<br>Inserted successfully<br>";
} else {
    echo "<br>Error creating table: " . $conn->error;
}
$conn->close();
?>

</body>
</html>