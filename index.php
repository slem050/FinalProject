<?php
$from=1;
$to=-1;
$type='undefined';
if(isset($_GET['from']) && isset($_GET['type']))
{
$from=$_GET['from'];
$to=$_GET['to'];
$type=$_GET['type'];
}

 ?>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library Navigation</title>
     <link rel="shortcut icon" href="//mw8.haifa.ac.il/pluginfile.php/1/theme_fordson/favicon/1557987900/univ_flag.png" />
    <link rel="stylesheet" href="https://cdn.pannellum.org/2.4/pannellum.css"/>
    <link rel="stylesheet" href="web_Style.css"/>
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

</head>
<body>
  <header>
<img id='imm' src="preferred/logo.jpg"></img>
</header>

<div id="panorama"></div>
<h2 class="w3-center">Integrated Points</h2>

<div class="w3-content w3-display-container" id="slides">


  <button class="w3-button w3-black w3-display-left" onclick="plusDivs(-1)">&#10094;</button>
  <button class="w3-button w3-black w3-display-right" onclick="plusDivs(1)">&#10095;</button>
</div>
<script>
 var from='<?php echo $from; ?>';
 var to='<?php echo $to; ?>';
 var type='<?php echo $type ?>'
</script>
   <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
   <script type="text/javascript" src="RequestAnimationFrame.js"></script>
   <script type="text/javascript" src="libpannellum.js"></script>
   <script type="text/javascript" src="pannellum.js"></script>
    <script src="script.js"></script>
   <script src="//netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>


</body>
</html>
