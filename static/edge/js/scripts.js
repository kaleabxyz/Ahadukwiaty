var panel = document.querySelector(".checkout");

function hide() {
    panel.setAttribute("aria-expanded", false);
}

function show() {
    panel.setAttribute("aria-expanded", true);
}

function showbtn(index, btn, id, size) {
    var buttons = document.querySelectorAll(".addtocart");
    var price = document.querySelectorAll(".price");
    var size_btn = document.getElementById(id);
    var size_btns = document.querySelectorAll(".small");
    size_btns.forEach((element) => {
        console.log(element);
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

    document.getElementById("flower_size_input_" + index).value = size;

    // buttons.forEach((button) => {
    //     button.setAttribute("aria-expanded", false);
    // });
    buttons[index - 1].setAttribute("aria-expanded", true);
}

function addToCart(productId) {
    var formData = new FormData(
        document.getElementById("add-to-cart-form-" + productId)
    );

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/add_to_cart/", true);
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Handle success, e.g., show a message to the user
            alert("Product added to cart successfully!");
        } else {
            // Handle errors
            alert("Error adding product to cart. Please try again later.");
        }
    };
    xhr.send(formData);
}

function removeCart(flower_id, flower_size) {
    console.log(flower_size);
    fetch("/remove_from_cart/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({
            flower_id: flower_id,
            flower_size: flower_size,
        }),
    })
        .then((response) => {
            if (response.ok) {
                loadCart();
            } else {
                // Handle errors or display a message to the user
                console.error("Error removing product from cart");
            }
        })
        .catch((error) => {
            console.error("Error removing product from cart:", error);
        });
}

function loadCart() {
    panel.setAttribute("aria-expanded", true);
    fetch("/get_cart/")
        .then((response) => response.json())
        .then((data) => {
            // Update the cart display on the page
            // For example, you can append the cart data to a <div> element
            console.log(data.total_price);
            document.getElementById("total_price").innerHTML = data.total_price;
            document.querySelector(".checkoutlists").innerHTML = data.html;
        })
        .catch((error) => {
            console.error("Error loading cart:", error);
        });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}
