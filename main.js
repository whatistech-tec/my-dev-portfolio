//Initialize lucide
lucide.createIcons();

//Initialize highlightjs
hljs.highlightAll();

/*======== NAVBAR START =========*/
const navbar = document.getElementById("navbar");
const routes = document.querySelectorAll("#navbar .nav__routes .route");
const sections = document .querySelectorAll("section");
window.onscroll = () => {
    if(window.scrollY > 100){
        navbar.classList.add("drop");
    }
    else{
       navbar.classList.remove("drop") ;
    }
    sections.forEach(section => {
        let top = window.scrollY;
        let offset = section.offsetTop - 100;
        let height = section.offsetHeight;
        let id = section.getAttribute("id");

        if(top >= offset && top < offset + height){
            routes.forEach((route) => {
                route.classList.remove("active");
                document
                    .querySelector("#navbar .nav__routes a[href*=" + id + "]")
                    .classList.add("active");
            });
        }
    });
};

/*======== SIDEBAR START =========*/
const menuBtn = document.getElementById("menu__btn");
const sidebar = document.querySelector(".sidebar");
const router = document.querySelectorAll(".sidebar .navlinks .navitem");
const navLinks = document.getElementById("navlinks");
const closeBtn = document.getElementById("close-sidebar-btn");

menuBtn.onclick = () => {
    sidebar.classList.toggle("visible");
};

sections.forEach(section => {
    let top = window.scrollY;
    let offset = section.offsetTop - 100;
    let height = section.offsetHeight;
    let id = section.getAttribute("id");

    if(top >= offset && top < offset + height){
        routes.forEach((route) => {
            route.classList.remove("active");
            document
                .querySelector(".sidebar .navlinks a[href*=" + id + "]")
                .classList.add("active");
        });
    }
});

closeBtn.onclick = () => {
    sidebar.classList.remove("visible");
};

navLinks.onclick = () => {
    sidebar.classList.remove("visible");
    
}

/*======== SIDEBAR END =========*/

//Theme switching
const themeCheckbox = document.getElementById('theme-checkbox');
const storageKey = "theme"
if(JSON.parse(localStorage.getItem(storageKey))){
    document.firstElementChild.setAttribute("data-theme","light");
    localStorage.setItem(storageKey,JSON.stringify(true));
    themeCheckbox.checked = true;
}else{
    document.firstElementChild.setAttribute("data-theme","dark");
    localStorage.setItem(storageKey,JSON.stringify(false));
    themeCheckbox.checked = false;
}
themeCheckbox.onchange = () => {
    if(themeCheckbox.checked){
        document.firstElementChild.setAttribute("data-theme","light");
        localStorage.setItem(storageKey,JSON.stringify(true));
        return
    }else{
        document.firstElementChild.setAttribute("data-theme","dark");
        localStorage.setItem(storageKey,JSON.stringify(false));
    }
}
/*======== NAVBAR END =========*/

/*======== HEADER START =========*/
const odometers = document.querySelectorAll(".odometer");
setTimeout(() => {
    odometers.forEach(list => {
        let id = list.getAttribute("id");
        if (id === "experience"){
            list.innerHTML = 6;
        }
        if (id === "project"){
            list.innerHTML = 150;
    
        }
        if(id === "awards"){
            list.innerHTML = 12;
        }
        if(id === "clients"){
            list.innerHTML = 800
        }
    })
},4000);
//gsap code
gsap
.timeline({delay:0.5})
.from("#header .points",{opacity:0, y:-30})
.from("#header .me",{opacity:0, scale:0.7})
.from(["#header .user__info .sub__title","#header .user__info .description"],{opacity:0, y: 20})
.from("#header .user__info .title",{opacity: 0, x: -30})
.from("#header .user__info .buttons",{opacity: 0, x: -30})
.from("#header .point",{opacity: 0, x: -30,stagger:0.5});
/*======== HEADER END =========*/


//Register ScrollTriggerPlugin
//gsap.registerPlugin(scrollTrigger);

/*======== ABOUT START =========*/
gsap.timeline({
    delay:0.5,
    scrollTrigger:{
        trigger: "#about",
        start: "20% bottom",
        end: "bottom top"
    },
})
.from("#about .box", {opacity: 0, y: 30,stagger: 0.5});
/*======== ABOUT END =========*/

/*======== SERVICES START =========*/
gsap.timeline({
    delay:0.5,
    scrollTrigger:{
        trigger: "#services",
        start: "20% bottom",
        end: "bottom top"
    },
})
.from(
    [
        "#services .section__header .sub__title",
        "#services .section__header .description",
    ],
    {opacity: 0, y: 30,stagger: 0.5}
)
.from("#services .service",{opacity:0, y: 30, stagger: 0.5});

/*======== SERVICES END =========*/

/*======== PROJECT START =========*/

/* //*****MIXITUP**** */
const filterButtons = document.querySelectorAll('.projects__categories li');
const fiterCards = e =>{
    document.querySelector('.filter-active').classList.remove('.filter-active');
    e.target.classList.add('.filter-active');
}

document.addEventListener('DOMContentLoaded', function(){
    var mixer = mixitup('.my-projects')
});

gsap.timeline({
    delay:0.5,
    
    scrollTrigger:{
        trigger: "#projects",
        start: "20% bottom",
        end: "bottom top"
    },
})
.from(
    [
        "#projects .section__header .sub__title",
        "#projects .section__header .description",
    ],
    {opacity: 0, y: 30,stagger: 0.5}
)
.from("#projects .project",{opacity:0, y: 30, stagger: 0.5});

/*======== PROJECT END =========*/

gsap.timeline({
    delay:0.5,
    scrollTrigger:{
        trigger: "#testimonials",
        start: "20% bottom",
        end: "bottom top"
    },
})
.from(
    [
        "#testimonials .section__header .sub__title",
        "#testimonials .section__header .description",
    ],
    {opacity: 0, y: 30,stagger: 0.5}
)
.from("#testimials .testimonial",{opacity:0, y: 30, stagger: 0.5});


/*======== CONTACT START =========*/
gsap.timeline({
    delay:0.5,
    scrollTrigger:{
        trigger: "#contact",
        start: "20% bottom",
        end: "bottom top",
    },
})
.from("#contact .box",{opacity:0, y:30, stagger:0.5})
.from("#contact .contact__form",{opacity:0, x:30});
/*======== CONTACT END =========*/





//svg icon implementation
/*
const dataCustomIcon = document.querySelectorAll("data-custom-icon");
dataCustomIcon.forEach((icon) => {
    if(icon.getAttribute("data-custom-icon")){
       const request = new MLHttpRequest();
       request.open("GET", "./assets/icons/" + icon.getAttribute("data-custom-icon") + ".svg");
       request.setRequestHeader("Content-Type", "image/svg+ml");
       request.addEventListener("load",(event) => {
        if(event.target.status === 200){
            const response = event.target.responseText;
            icon.innerHTML = response;
        }
       });
       request.send();
    }
});*/

