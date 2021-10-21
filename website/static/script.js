const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})


function showPopup() {
    let popup = document.getElementById("popup");
    popup.style.display = "block";
}

function hidePopup() {
    let popup = document.getElementById("popup");
    popup.style.display = "none";
}

function showEditTask(task_id) {
    var div_id = "edit-task-container-" + task_id;
    console.log(div_id);
    let popup = document.getElementById(div_id);
    popup.style.display = "block";
}

function hideEditTask(task_id) {
    var div_id = "edit-task-container-" + task_id;
    console.log(div_id);
    let popup = document.getElementById(div_id);
    popup.style.display = "none";
}

function showChangePassPopUp() {
    let popup = document.getElementById("changePassPopup");
    popup.style.display = "block";
}

function hideChangePassPopUp() {
    let popup = document.getElementById("changePassPopup");
    popup.style.display = "none";
}

function submit(){
    document.editAccountForm.submit();
}
