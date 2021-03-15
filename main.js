// NavBar

function hideicon(){
    var menuicon = document.getElementById("menu");
    var navigation = document.getElementById("navigation");
    menuicon.setAttribute("style","display:none;");
    navigation.classList.remove("hide");
}

function showicon(){
    var menuicon = document.getElementById("menu");
    var navigation = document.getElementById("navigation");
    menuicon.setAttribute("style","display:block;");
    navigation.classList.add("hide");
}

// comment 
function showcomment(){
    var comment = document.getElementById("comment");
    comment.setAttribute("style","display:block;");
}
