const title = document.title;
// console.log(`The title is: ${title}`)

const navTabs = document.getElementsByClassName('nav-link');
// console.log(navTabs);

for (tab of navTabs){
    // console.log(tab.innerText);
    if (tab.innerText == title) {
        // console.log(tab)
        tab.classList.add('active');
    }
}
