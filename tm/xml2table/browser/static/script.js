function tab(tabid) {

    document.getElementById(tabid).style.display = "block";
    document.getElementById("t" + tabid).className = "current";

	if (tabid == "tab5") {
        document.getElementById("tab6").style.display = "none";
        document.getElementById("ttab6").className = "";
		
		/////////stuck here
		var counter = 0;
		var counter1 = 0;
		
		$("#tab5 table tr td").each(function() { if($(this).html().toLowerCase()=='fail'){	counter++;	}	});	
		$('#count_div1').html(counter+'&nbsp;');
		
		$("#tab6 table tr td").each(function() { if($(this).html().toLowerCase()=='fail'){	counter1++;	}	});	
		$('#count_div2').html(counter1+'&nbsp;');
		/////////stuck here		
    } 
	
	if (tabid == "tab6") {
        document.getElementById("tab5").style.display = "none";
        document.getElementById("ttab5").className = "";
		
		/////////stuck here
		var counter = 0;
		var counter1 = 0;
		
		$("#tab5 table tr td").each(function() { if($(this).html().toLowerCase()=='fail'){	counter++;	}	});	
		$('#count_div1').html(counter+'&nbsp;');
		
		$("#tab6 table tr td").each(function() { if($(this).html().toLowerCase()=='fail'){	counter1++;	}	});	
		$('#count_div2').html(counter1+'&nbsp;');
		/////////stuck here		
    } 
	
}    
        
$(document).ready(function() {
    var counter = 0;
    var counter1 = 0;
    
    $("#tab5 table tr td").each(function() { if($(this).html().toLowerCase()=='fail'){  counter++;  }   }); 
    $('#count_div1').html(counter+'&nbsp;');
    
    $("#tab6 table tr td").each(function() { if($(this).html().toLowerCase()=='fail'){  counter1++; }   }); 
    $('#count_div2').html(counter1+'&nbsp;');
});
	