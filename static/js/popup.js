var top0=left0=0;

if (window.ActiveXObject) {
        // IE
        top0 = 0;
	left0 = 0;    
} else if (document.getBoxObjectFor){
        // Firefox
	top0 = 0;
	left0 = 0; 
} else if (window.MessageEvent && !document.getBoxObjectFor){
        // Google Chrome
	top0 = 40;
	left0 = 0;  
 }else if (window.opera) {
        // Opera
	top0 = 0;
	left0 = 0;  
 }else if (window.openDatabase) {
        // Safari
	top0 = 0;
	left0 = 0;  
 }

function $(d){return document.getElementById(d);}

function addContent(obj,content){
	$("PopupBody").innerHTML+= "<tr> <td>"+content+"</td><td>8</td></tr>";
}

function findPos(obj) {
	var curleft = curtop = 0;
	if (obj.offsetParent) {
		curleft = obj.offsetLeft
		curtop = obj.offsetTop
		while(obj = obj.offsetParent) {
		     curleft += obj.offsetLeft
	  		curtop += obj.offsetTop
		}
	}
	curtop += top0;
	curleft +=left0;
	return [curleft,curtop];
}

function display_menu(parent,offX,offY,named,content){
        var sourceName= new Array("NCBI-Bacteria",
 		"BGI-GUT&nbsp;&nbsp;",
		"CAZy&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
                "CAMERA&nbsp;&nbsp;",
                "NCBI-env-nr&nbsp;&nbsp;",
		"NCBI-Fungi&nbsp;&nbsp;",
	         "WUSTL-gut&nbsp;&nbsp;",
 		"JGI&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
                "NCBI-nr&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
                "Phytozome-Plant&nbsp;&nbsp;&nbsp;&nbsp;",
 		"Cow-Rumen&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
                "Swiss-Prot;&nbsp;&nbsp;&nbsp;&nbsp;",
                "TrEMBL&nbsp;&nbsp;&nbsp;");
        
	var strArr=content.split("|");
        $("PopupBody").innerHTML="<table id=PopupTab width=101 border=0 cellpadding=0 cellspacing=0>";
	for(i=0,j=0;i<13;i++) {
	   if(strArr[i].charAt(0)!="0"&&strArr[i].charAt(0)!="-") {
	       if(j==0) {
		     $("PopupBody").innerHTML+="<tr> <td width=60>"+sourceName[i]+"</td> <td width=20>"+strArr[i]+"<br /></td></tr>";
		   } else {
		    $("PopupBody").innerHTML+="<tr> <td>"+sourceName[i]+"</td><td>"+strArr[i]+"<br /></td></tr>";
		   }
		   j++;		   
	   }
                $("PopupBody").innerHTML+="</table>";
        }
	//override the 'display:none;' style attribute
	$(named).style.display = "";
	//get the placement of the element that invoked the <strong class="highlight">menu</strong>...
	var placement = findPos(parent);
	//...and put the <strong class="highlight">menu</strong> there
	$(named).style.left = placement[0] +offX+ "px";
	$(named).style.top = placement[1] +offY+ "px";
}

function hide_menu(named){
	$(named).style.display = "none";
}
