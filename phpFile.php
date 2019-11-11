<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "Virtual_map";
// Create connection
function connect()
{
  $conn = new mysqli($GLOBALS['servername'], $GLOBALS['username'], $GLOBALS['password'],
  $GLOBALS['dbname']);
  // Check connection
  if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
return $conn;
}
function getNode($num)
{
  $conn=connect();
$sql = "SELECT * FROM node where id='$num'";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
// output data of each row
$row = $result->fetch_assoc();
$id=$row['id'];
$area_type=$row['area type'];
$books_range=$row['books range'];
$rooms_range=$row['rooms range'];
$toilets=$row['toilets'];
$node='{"id":'.$id.',"area_type":'.$area_type.',"books_range:'.$books_range.',"rooms_range":'.$rooms_range.',"toilets":'.$toilets.'}';
return $node;
//while($row = $result->fetch_assoc())
//echo "id: " . $row["id"];

} else {
echo "0 results";
}
$conn->close();
}
function getHotSpots($num)
{
    $r=0;
    $spots='';
    $conn=connect();
    $sql = "SELECT * FROM hotspot where ID1='$num'";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
    // output data of each row
    $count=0;
    while($row = $result->fetch_assoc()) {
    /*  if($count!=0)
      $spots.=',';
      else{
        $count=$count+1;
      }*/
      $id=$row["ID2"];
      $pitch=$row["pitch"];
      $yaw=$row["yaw"];
      $spots.='{"id":'.$id.',"pitch":'.$pitch.',"yaw":'.$yaw.',"clickHandlerArgs":'.$id.', "cssClass": "park-hot-spot hs-park-overview"}*';
    }
    return $spots;
} else {
    echo "0 results";
}
}
function getPointsIds()
{
  $conn=connect();
  $points='';
  $sql = "SELECT * FROM predefinedspots";
  $result = $conn->query($sql);
  if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
      $id=$row["id"];
      $info=$row["info"];
      $points.='{"id":'.$id.',"info":"'.$info.'"}*';
  
}
}
return $points;
}

?>
