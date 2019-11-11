<?php
error_reporting(E_ERROR | E_PARSE);
if(isset($_GET['page']))
$num=$_GET['page'];
else {
  $num=1;
}
 ?>
<html>
<head>
  <link rel="stylesheet" href="style-simple.css">
</head>
  <body>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script type="text/javascript" src="simple-js.js"></script>
    <!-- Demo stuff-->
    <main>
      <p class="ft">this is the haifa university navigation site, please choose one of the following so we can guide you to the closest point.</p>
      <p><a href="https://twitter.com/ettrics/" target="_blank"><i class="fa fa-twitter"></i></a></p><img class="plate" src="preferred/logo2.jpg" alt=""/>
    </main>
    <!-- Component starts here-->
    <ul class="blocks-names">
      <li class="blocks__name">Book</li>
      <li class="blocks__name">Bathroom</li>
      <li class="blocks__name">Room</li>

    </ul>
    <ul class="blocks">
      <li class="blocks__block" id="1"></li>
      <li class="blocks__block" id="2"></li>
      <li class="blocks__block" id="3"></li>

    </ul>
    <ul class="blocks-content">
      <li class="blocks-content__content">
        <div class="content__close"></div>
        <h2>Book</h2>
        <p>you will be redirected to the Library offical site where you will search for your book, you will find an option for navigation on the left site,click it so we can navigate you</p><i class="blocks__content-close fa fa-close"></i>
        <a href="https://haifa-primo.hosted.exlibrisgroup.com/primo-explore/search?vid=HAU&lang=iw_IL">Link</a>
      </li>
      <li class="blocks-content__content">
        <h2>Bathrooms</h2>
        <p>you will be directed to the closest bathroom to you,please press ok to continue</p><i class="blocks__content-close fa fa-close"></i>
        <button class="prssbtn"></button>
      </li>
      <li class="blocks-content__content">
        <h2>Rooms</h2>
        <p>please enter the room number.</p><button class="blocks__content-close fa fa-close"></button>
        <input name='page' type="text" id='rmpt' required>
        <button class="button1" id="btn">Confirm</button>
      </li>
      <script>
      var from='<?php echo $num ?>';
      </script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script type="text/javascript" src="simple-js.js"></script>
      <script src="simpleScript.js"></script>

    </ul>
  </body>
</html>
