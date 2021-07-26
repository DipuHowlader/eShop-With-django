document.addEventListener("DOMContentLoaded", (e) => {
  const loader = document.querySelector("#loader");
  const message = document.getElementById("message");
  setTimeout(() => {
    loader.classList.add("vanish");
  }, 200);

  if (message) {
    setTimeout(() => {
      message.style.right = "-50%";
    }, 2500);
  }
});
