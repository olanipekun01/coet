document.addEventListener("DOMContentLoaded", () => {
    const triggers = document.querySelectorAll(".accordion-trigger");
  
    triggers.forEach((trigger) => {
      trigger.addEventListener("click", () => {
        const target = document.getElementById(trigger.getAttribute("data-target"));
        const chevron = trigger.querySelector(".chevron");
  
        // Toggle the content
        if (target.classList.contains("hidden")) {
          target.classList.remove("hidden");
          chevron.textContent = "▲";
        } else {
          target.classList.add("hidden");
          chevron.textContent = "▼";
        }
      });
    });
  });