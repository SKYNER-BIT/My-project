let btn = document.getElementById("add-subject")
let pop = document.getElementById("win-pop")
let createbtn = document.createElement("button")
let open = false

btn.addEventListener("click", () => {
    if (open) {
        pop.style.display = "none";
        open = false;
    } else {
        pop.style.display = "flex";
        open = true;
    }
})