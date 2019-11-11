<?php
/* Getting file name */
include 'phpFile.php';
if (isset($_POST["num"])){
$filename = $_POST['num'];

/* Location */
$location = "images/".$filename;
$uploadOk = 1;
$imageFileType = "jpg";

/* Valid Extensions */
$valid_extensions = array("jpg","jpeg","png");
/* Check file extension */
if( !in_array(strtolower($imageFileType),$valid_extensions) ) {
   $uploadOk = 0;
}

if($uploadOk == 0){
   echo 0;
}else{
   /* Upload file */
      echo $location.".".$imageFileType;
}
}
if (isset($_POST["n"])){
  $number=$_POST['n'];
  echo getHotSpots($number);

}
if(isset($_GET["rimg"]))
{

    header("Content-Type: image/png");
    $name=$_GET['rimg'].'.jpg';
    $file = file_get_contents("preferred/".$name);
    echo base64_encode($file);

}

if(isset($_GET["p"]))
{

  echo getPointsIds();

}


  ?>
