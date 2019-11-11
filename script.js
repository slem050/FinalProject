document.body.style.backgroundImage =LoadImg('background');
window.mobileAndTabletcheck = function() {
  var check = false;
  (function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))) check = true;})(navigator.userAgent||navigator.vendor||window.opera);
  return check;
};
var viewer;
var hotspots;
var hotSpotsIds=new Array();
var previuseHotSpot=new Array();
var featureHotSpots=new Array();
var slideIndex = 1;
var sortprefix=0;
//showDivs(slideIndex);
loading();
loadPoints()
function loading()
{
  if(type=="undefined")
  {
    id=1;
  }else {
    if(type=="room")
    {
      sortprefix=1;
      id=parseInt(from);
      featureHotSpots=getDestination(to).filter(function (value) {
    return !Number.isNaN(value);
});

    }
}
     openModal(null,id)
}
function changeUpload()
{
}
function gethotspots(p1)
{
hotspots=new Array();
var newUs ="createTooltipFunc" ;
var newValue= hotspot;
var newUs1 ="createTooltipArgs" ;
var newValue1= "";
var newUs2 ="clickHandlerFunc" ;
var newValue2= openModal;
    var strings=new Array();
    $.ajax({
            url: 'handleRequests.php',
            type: 'POST',
            data: {n: id},
            async: false,
            success: function(response){
              hotspots=response;
            },
            }
        );

        var jsons=hotspots.split('*');
        jsons=jsons.filter(function (el) {
  return el != "";
});

        for(var i=0;i<jsons.length;i++)
        {
          var obj = JSON.parse(jsons[i]);
          obj[newUs]=newValue;
          obj[newUs2]=newValue2;
          if(featureHotSpots.indexOf(obj['id'])!=-1)
          strings.push(obj);

          hotSpotsIds.push(obj['id']);

        }
        console.log(strings);
        console.log(featureHotSpots);
        console.log(previuseHotSpot);
        return strings;
}
function removeHotspots()
{
  for(var i=0;i<hotSpotsIds.length;i++)
  {
    viewer.removeHotSpot(hotSpotsIds[i]);
  }
  hotSpotsIds=new Array();
}
function arrayRemove(arr, value) {
  var index = arr.indexOf(value);
if (index !== -1) arr.splice(index, 1);

}
function manageHotSpots()
{
    if(previuseHotSpot.length==0 && featureHotSpots.length==0)
    return;
    else {
      var index = featureHotSpots.indexOf(id);
if (index > -1) {
  featureHotSpots.splice(index, 1);
    }
    if(previuseHotSpot.indexOf(id)==-1)
    previuseHotSpot.push(id);
}
}
function  openModal(event,args){
  if(id==to)
  {
    alert("you have arrived to your distination");

  }
  else {
    manageHotSpots();

  }
  if(sortprefix==1)
  id=args;
  if(viewer!=null)
  removeHotspots();
viewer = pannellum.viewer('panorama', {
   "type": "equirectangular",
   "autoRotate": -2,
   "panorama": "/images/"+args+".jpg",
   "hotSpots": gethotspots(args) ,
   "autoLoad": true,
   "hfov":150

});
}
function getPoints()
{
    var ids=new Array();
  $.ajax({
          url: 'handleRequests.php',
          type: 'GET',
          data: {p: 0},
          async: false,
          success: function(response){

            var jsons=response.split('*');
            jsons=jsons.filter(function (el) {
      return el != "";
      });
      for(var i=0;i<jsons.length;i++)
      {
        var obj = JSON.parse(jsons[i]);
        ids.push(obj);
      }

          },
          }
      );
      return ids;
}
function LoadImg(filename) {
  var value;
          $.ajax({
          url: 'handleRequests.php',
          type: 'get',
          datatype:'html',
          data:{'rimg':filename},
          async: false,
          crossDomain: 'true',
          success: function(data, status) {
              value = data;
          }
  });
  return value;
}
function loadPoints()
{
 var arr=getPoints();
 for(var i=0;i<arr.length;i++)
 {
   var obj=arr[i];
   var elem = document.createElement("img");
   elem.setAttribute("src", 'data:image/jpg;base64,' + LoadImg(obj['id']));
   elem.setAttribute("class", "mySlides");
   document.getElementById("slides").appendChild(elem);
 }
}
function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";
}
function getDestination(room)
{
  var value;
  var code="2/2/"+room;
  $.ajax({
  url: 'handleRequests.php',
  type: 'get',
  datatype:'html',
  data:{'destination':from,'code':code},
  async: false,
  crossDomain: 'true',
  success: function(data, status) {
      value=data;
  }
});
mystring = value.replace('[','');
mystring = value.replace(']','');
value=mystring.split(',').map(function(item) {
    return parseInt(item, 10);
});
return value;
}
function hotspot(hotSpotDiv, args) {
       hotSpotDiv.classList.add('custom-tooltip');
       var span = document.createElement('span');
       span.innerHTML = args;
       hotSpotDiv.appendChild(span);
       span.style.width = span.scrollWidth - 20 + 'px';
       span.style.marginLeft = -(span.scrollWidth - hotSpotDiv.offsetWidth) / 2 + 'px';
       span.style.marginTop = -span.scrollHeight - 12 + 'px';
   }
