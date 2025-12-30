const openBtn = document.getElementById("openStudentModal")
const modal = document.getElementById("modal-student")
const closeBtn = document.getElementById("closeStudentModal")

const tabButtons = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');


/* Modal Tab consts */
const modalTabList = ['personal', 'academic', 'contact', 'address'];
let currentTabIndex = 0;

/* Open Student Modal */
openBtn.addEventListener("click", (e) =>
{
    e.preventDefault();
    modal.classList.add("active");
});

/* Close Student Modal */
closeBtn.addEventListener("click", (e) =>
{
    e.preventDefault();
    modal.classList.remove("active");
})

/* Deactive the modal in the window */
modal.addEventListener("click", (e) =>
{
    if (e.target === modal) {
        modal.classList.remove("active");
    }
});


/* Alter the current tab in the Student modal */
function switchTab(tabName) {
    /* Content */
    tabContents.forEach(tab => tab.classList.remove('active'));
    document.getElementById(`${tabName}-tab`).classList.add('active');

    /* Buttons */
    tabButtons.forEach(btn => btn.classList.remove('active'));
    document.querySelector(`.tab-btn[data-tab="${tabName}"]`).classList.add('active')

    /* Index */
    currentTabIndex = modalTabList.indexOf(tabName);
    document.getElementById("current-tab").textContent = currentTabIndex + 1;
}

/* Buttons Click */
tabButtons.forEach(button => {
    button.addEventListener("click", () => {
        switchTab(button.dataset.tab);
    });
});

/* NEXT / PREV */
function nextTab() {
    if (currentTabIndex < modalTabList.length - 1) {
        switchTab(modalTabList[currentTabIndex + 1]);
    }
}

function prevTab() {
    if (currentTabIndex > 0) {
        switchTab(modalTabList[currentTabIndex - 1]);
    }
}