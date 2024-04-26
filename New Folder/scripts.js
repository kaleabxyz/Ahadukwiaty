var panel = document.querySelector(".checkout");

function hide() {
    panel.setAttribute("aria-expanded", false);
}

function show() {
    panel.setAttribute("aria-expanded", true);
}

function showbtn(index) {
    var buttons = document.querySelectorAll(".addtocart");
    buttons.forEach((button)=>{
        button.setAttribute("aria-expanded", false);
    });
    buttons[index - 1].setAttribute("aria-expanded", true);
}
