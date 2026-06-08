let btn = document.getElementById("add-subject");
let pop = document.getElementById("win-pop");
let tracker = document.getElementById("tracker-header");
const uniqueId = `item-${crypto.randomUUID()}`;
let submit = document.getElementById("submit");
let subjectinput = document.getElementById("subject-name");
let open = false;

btn.addEventListener("click", () => {
    open = !open;

    if (open) {
        pop.style.opacity = "1";
        pop.style.transform = "translateY(0px)";
        pop.style.visibility = "visible";
        pop.style.display = "flex";
    } else {
        pop.style.opacity = "0";
        pop.style.transform = "translateY(-5px)";
        pop.style.visibility = "hidden";
        pop.style.display = "none";
    }
});
submit.addEventListener("click", (e) => {
    e.preventDefault();

    let subject = subjectinput.value;

    let div = document.createElement("div");
    let del = document.createElement("button");
    let header = document.createElement("h3");

    header.textContent = subject;
    del.textContent = "Del";

    div.style.width = "500px";
    div.style.height = "70px";
    div.style.border = "1px solid black";
    div.style.background = "rgba(115, 125, 125,0.2)";
    div.style.margin = "5px auto";
    div.style.borderRadius = "5px";

    div.style.display = "flex";
    div.style.justifyContent = "space-between";
    div.style.alignItems = "center";

    header.style.margin = "0";

    del.style.width = "40px";
    del.style.height = "40px";
    del.style.background = "rgb(58, 58, 144)";
    del.style.color = "white";

    del.addEventListener("click", () => {
        div.remove();
    });

    div.appendChild(header);
    div.appendChild(del);
    tracker.appendChild(div);
});