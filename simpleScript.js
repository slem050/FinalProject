var to="";
document.getElementById('btn').addEventListener("click", function(){
  var fm=document.getElementById('rmpt').value;
  if(fm.length==0  || isNaN(fm) || fm<=1 || fm>=400 )
  {
  alert('insert correct value please');
  return;
  }
  to=fm;
  sendrequest('room');

})
function sendrequest(gend)
{
  $.ajax({
          url: 'managePython.php',
          type: 'GET',
          data: {type : gend,
            from : from,
            to : to},
          async: false,
          success: function(response){
            console.log(response);
            //hotspots=response;
          },
          }
      );
  //  window.location.href="index.php?from="+from+"&to="+to+"&type="+gend;
}
