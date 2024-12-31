$(document).ready(function() {
	$('.tabular.menu .item').tab();
	$('.ui.dropdown.link.item').dropdown();
	$("table.data").dataTable({
		"responsive": true,
		"bStateSave" : true, 
		"bJQueryUI": true, 
		"sPaginationType": "full_numbers", 
		"iDisplayLength": 15,
		"aLengthMenu": [[15, 30, 50, -1], [15, 30, 50, "All"]]
	});
	$("#CGC").dataTable({
		"bJQueryUI": true, 
		"sPaginationType": "full_numbers", 
		"iDisplayLength": 15,
		"order": [],
		"ordering": false,
		"aLengthMenu": [[15, 30, 50, -1], [15, 30, 50, "All"]]
	});
	$("#Overview").dataTable({
		"bJQueryUI": true, 
		"bStateSave" : true, 
		"sPaginationType": "full_numbers", 
		"iDisplayLength": 15,
		"aLengthMenu": [[15, 30, 50, -1], [15, 30, 50, "All"]]
	});
});
