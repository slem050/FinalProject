<?php
if(isset($_GET['type']))
{
  if($_GET['type']=='room')
  {

    //if(isset($_GET["destination"]) && isset($_GET["code"]))
    {
      $output = system('python C:/xampp/htdocs/GetPath.py '.$_GET["from"].' 1/2/'.$_GET['to'].' >c:\xampp\htdocs\mk.txt');
      $fh = fopen('mk.txt','r');
      $line = fgets($fh);
       echo($line);
    }

  }
}







 ?>
