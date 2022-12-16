//color of links to change on click
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('link');

forEach(link => {
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
})



//to toggle faqs

const faq = document.querySelectorAll(".faqs")

faq.forEach((faqs) => {
  faqs.addEventListener("click", () => {
    faqs.classList.toggle("active");
  });
});

