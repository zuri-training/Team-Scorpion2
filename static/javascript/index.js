//color of four links to change on click
document.querySelector(".links").onclick=ev=>{if(ev.target.tagName=="A")
  ev.target.className="done"
}


//to toggle faqs

const faq = document.querySelectorAll(".faqs")

faq.forEach((faqs) => {
  faqs.addEventListener("click", () => {
    faqs.classList.toggle("active");
  });
});