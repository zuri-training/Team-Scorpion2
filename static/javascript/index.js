//color of four links to change on click
const links = document.querySelectorAll(".link")

links.forEach((link) => {
  link.addEventListener("click", () => {
    link.classList.toggle("active");
  });
});


//to toggle faqs

const faq = document.querySelectorAll(".faqs")

faq.forEach((faqs) => {
  faqs.addEventListener("click", () => {
    faqs.classList.toggle("active");
  });
});

