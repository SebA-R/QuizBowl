const checkbox = document.querySelector('input[name=contrast]');
const bodyStyles = document.body.style;
const root = document.documentElement;
const mouseCenter = document.getElementById("mouse-center");
const mouse = document.getElementById("mouse");
let mouseX = 0;
let mouseY = 0;

const lerpingFactor = 0.8; // Adjust the lerping factor for desired lag effect
let lerpedX = 0;
let lerpedY = 0;


checkbox.addEventListener('change', () => {
    bodyStyles.setProperty('--background-color', checkbox.checked ? '#FFFFFF' : '#1f2029');
    bodyStyles.setProperty('--text-color', checkbox.checked ? '#1f2029' : '#FFFFFF');
    bodyStyles.setProperty('--header-color', checkbox.checked ? '#102770' : '#ffeba7');
    bodyStyles.setProperty('--accent-color', checkbox.checked ? '#ffeba7' : '#102770');
    bodyStyles.setProperty('--secondary-color', checkbox.checked ? '#ebebeb' : '#2a2b38');
    
    localStorage.setItem(checkbox.value, checkbox.checked);
});

if (localStorage.getItem(checkbox.value) == "true") {
    checkbox.checked = true;
}
bodyStyles.setProperty('--background-color', checkbox.checked ? '#FFFFFF' : '#1f2029');
bodyStyles.setProperty('--text-color', checkbox.checked ? '#1f2029' : '#FFFFFF');
bodyStyles.setProperty('--header-color', checkbox.checked ? '#102770' : '#ffeba7');
bodyStyles.setProperty('--accent-color', checkbox.checked ? '#ffeba7' : '#102770');
bodyStyles.setProperty('--secondary-color', checkbox.checked ? '#ebebeb' : '#2a2b38');

function updateMousePosition(scrollX, scrollY) {
    lerpedX += (mouseX - lerpedX) * lerpingFactor;
    lerpedY += (mouseY - lerpedY) * lerpingFactor;


    mouse.setAttribute("style", `left: ${lerpedX - 20 + scrollX}px; top: ${lerpedY - 20 + scrollY}px;`);
    mouseCenter.setAttribute("style", `left: ${mouseX + scrollX}px; top: ${mouseY + scrollY}px;`);
}

function handleMouseMove(event) {
    mouseX = event.clientX;
    mouseY = event.clientY;

    updateMousePosition(window.scrollX, window.scrollY);
}

function handleScroll() {
    updateMousePosition(window.scrollX, window.scrollY);
}

root.addEventListener("mousemove", handleMouseMove);
window.addEventListener("scroll", handleScroll);

document.addEventListener('click', () => {
    mouse.classList.add("click");

    setTimeout(() => {
        document.querySelector('.click').classList.remove('click');
    }, 600);
});

