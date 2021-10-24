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


// calendar code
isLeapYear = (year) => {
    return (year%4 === 0 && year%100 !== 0 && year%400 !== 0) || (year%100 === 0 && year%400 === 0)
}

getFebDays = (year) => {
    return isLeapYear(year) ? 29 : 28
}

let calendar = document.querySelector('.calendar')

const month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

let month_picker = document.querySelector('#month-picker')

month_picker.onclick = () => {
    month_list.classList.add('show')
}

// generate calendar
generateCalendar = (month, year) => {
    let calendar_days = document.querySelector('.calendar-days')
    let calendar_header_year = document.querySelector('#year')

    calendar_days.innerHTML = ''

    let days_of_month = [31, getFebDays(year), 31 ,30, 31, 30, 31, 31, 30, 31, 30, 31]

    month_picker.innerHTML = month_names[month]
    calendar_header_year.innerHTML = year

    let first_day = new Date(year, month, 1)
    if (first_day.getDay() === 0) {
        for(let i = 1; i <= days_of_month[month] + 7 - 1 ; i++) {
            let day = document.createElement('div')
    
            if(i >= 7) {
                day.classList.add('calendar-day-hover')
                day.innerHTML = i - 7 + 1
            }
    
            calendar_days.appendChild(day)
        }
    }
    else {
        for(let i = 1; i <= days_of_month[month] + first_day.getDay() - 1 ; i++) {
            let day = document.createElement('div')
    
            if(i >= first_day.getDay()) {
                day.classList.add('calendar-day-hover')
                day.innerHTML = i - first_day.getDay() + 1
            }
    
            calendar_days.appendChild(day)
        }
    }
}

let month_list = calendar.querySelector('.month-list')

month_names.forEach((e, index) => {
    let month = document.createElement('div')
    month.innerHTML = `<div>${e}</div>`
    month.onclick = () => {
        month_list.classList.remove('show')
        curr_month.value = index
        generateCalendar(curr_month.value, curr_year.value)
    } 
    month_list.appendChild(month)
})

document.querySelector('#prev-year').onclick = () => {
    --curr_year.value
    generateCalendar(curr_month.value, curr_year.value)
}

document.querySelector('#next-year').onclick = () => {
    ++curr_year.value
    generateCalendar(curr_month.value, curr_year.value)
}

let currDate = new Date()
let curr_month = {value: currDate.getMonth()}
let curr_year = {value: currDate.getFullYear()}

generateCalendar(curr_month.value, curr_year.value)