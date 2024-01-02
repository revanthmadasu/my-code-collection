

<html>
<body>
    <form action="" method="POST">
		Department Name: <input type="text" name="dept_name"><br>
        <input type="submit" name="submit" value="Search" />
    </form>
</body>
</html>

<?php
if(isset($_POST['submit'])){
	if(empty($_POST['dept_name'])){
		echo "Enter a search term";
	}
  
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
		//echo "Successfully connected";
	}
  
	$query=$_POST['dept_name'];
	//echo $query;
  
	$sql = "select budget from department where dept_name = '$query'";
	$result = $conn->query($sql);
	echo "<br/>Results: Total Budget is ";
	$values = $result->fetch_assoc();
	echo $values["budget"];	
	
	//terminate connection
	$conn->close();
}
?>