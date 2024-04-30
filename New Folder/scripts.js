var panel = document.querySelector(".checkout");

function hide() {
    panel.setAttribute("aria-expanded", false);
}

function show() {
    panel.setAttribute("aria-expanded", true);
}

function showbtn(index, btn, id) {
    var buttons = document.querySelectorAll(".addtocart");
    var price = document.querySelectorAll(".price");
    var size_btn = document.getElementById(id);
    var size_btns = document.querySelectorAll(".small");
    size_btns.forEach((element) => {
        // console.log(element);
        if (index * 10 < element.id && element.id < (index + 1) * 10) {
            element.classList.remove("border");
        }
    });

    price.forEach((element) => {
        if (element.id == index) {
            element.innerHTML = btn;
            size_btn.classList.add("border");
            // Perform actions on the element with the specific ID
            // console.log('Element with ID "specificId" found:', element);
        }
    });

    // buttons.forEach((button) => {
    //     button.setAttribute("aria-expanded", false);
    // });
    buttons[index - 1].setAttribute("aria-expanded", true);
}

const firstDiv = document.getElementById("popup");
const secondDiv = document.getElementById("po");

let isVisible = true; // Track the visibility state of the first div

document.addEventListener("click", function (event) {
    if (!secondDiv.contains(event.target)) {
        if (isVisible) {
            firstDiv.style.display = "none";
            isVisible = false;
        }
    } else {
        if (!isVisible) {
            firstDiv.style.display = "block";
            isVisible = true;
        }
    }
});
