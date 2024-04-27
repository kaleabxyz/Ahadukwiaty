var panel = document.querySelector(".checkout");

function hide() {
  panel.setAttribute("aria-expanded", false);
}

function show() {
  panel.setAttribute("aria-expanded", true);
}

function showbtn(index) {
  var buttons = document.querySelectorAll(".addtocart");
  buttons.forEach((button) => {
    button.setAttribute("aria-expanded", false);
  });
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

const descriptionDiv = document.getElementById("description");
const descriptionPartDiv = document.getElementById("descriptionpart");
const reviewDiv = document.getElementById("review");
const reviewPartDiv = document.getElementById("reviewpart");

descriptionPartDiv.style.display = "block"; // Initially show description part

function toggleBorder(clickedDiv, otherDiv, borderStyle) {
  clickedDiv.style.borderTop = borderStyle;
  otherDiv.style.borderTop = "none";
}

descriptionDiv.addEventListener("click", () => {
  toggleBorder(descriptionDiv, reviewDiv, "1px solid black");
  descriptionPartDiv.style.display = "block";
  reviewPartDiv.style.display = "none";
});

reviewDiv.addEventListener("click", () => {
  toggleBorder(reviewDiv, descriptionDiv, "1px solid black");
  descriptionPartDiv.style.display = "none";
  reviewPartDiv.style.display = "block";
});


