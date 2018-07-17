<html>
<style>
body {
    background-color: #CCCCCC;
}

</style>

<body>

<?php
error_reporting(E_ALL);
ini_set('display_errors','On');
?>


<?php

/// DB connection 
$host = "localhost";
//$host = "127.0.0.1";
$user = "vpalladi";
$pass = "vito8a82";
$db = "testRiki";

echo "my  server  is  " . $host . "<br>";

echo "DB : " . $db . "<br>";

$conn = new mysqli($host, $user, $pass, $db);

if ( $conn->connect_error ) {
    die(">>> Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";

// self-update dropdown menu ###
$result = mysqli_query($conn, "SELECT id FROM orders");
$select= '<select name="test">';
$select.='<option value="">orderId</option>';

while( $rs = $result->fetch_row() ){
    $select.='<option value="'.$rs[0].'">'.$rs[0].'</option>';
}
$select.='</select>';
echo $select;


// test queries
$queryOperators = "SELECT m.name FROM operators o 
INNER JOIN machines_operators mo ON mo.operator_id = o.id 
INNER JOIN machines m ON m.id = mo.machine_id 
WHERE o.name = 'riccardo' AND o.surname='di'";

$queryProduction = "SELECT prod.order_id,prod.quantity FROM production prod 
INNER JOIN orders o ON o.id = prod.order_id 
WHERE prod.order_id=1";

$result = mysqli_query($conn, $queryProduction);

while ($row = $result->fetch_row()) {
    //var_dump($row);
    echo "<br>" . $row[0] . " " . $row[1];
}

$queryProduction = "SELECT o.id,o.quantity FROM orders o 
WHERE o.id=1";

$result = mysqli_query($conn, $queryProduction);

while ($row = $result->fetch_row()) {
    //var_dump($row);
    echo "<br>" . $row[0] . " " . $row[1];
}

$conn->close();

?>

</body>
</html>
