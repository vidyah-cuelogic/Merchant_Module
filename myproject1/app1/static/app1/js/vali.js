function AlertIt() {
    var answer = confirm("Please click on OK to continue.")
    if (answer)
        window.location = "http://www.continue.com";
}

function toggle() {
    var ele = document.getElementById("toggleText");
    var text = document.getElementById("displayText");
    if (ele.style.display == "block") {
        ele.style.display = "none";
    } else {
        ele.style.display = "block";
    }
}
