document.addEventListener("DOMContentLoaded", (event) => {
  function toggleNavbar(collapseID) {
    document.getElementById(collapseID).classList.toggle("hidden");
    document.getElementById(collapseID).classList.toggle("bg-white");
    document.getElementById(collapseID).classList.toggle("m-2");
    document.getElementById(collapseID).classList.toggle("py-3");
    document.getElementById(collapseID).classList.toggle("px-6");
  }

  (window as any).toggleNavbar = toggleNavbar;
  /* Function for dropdowns */
  function openDropdown(event, dropdownID) {
    let element = event.target;
    while (element.nodeName !== "A") {
      element = element.parentNode;
    }
    (window as any).openDropdown = openDropdown;
    // var popper = new Popper(element, document.getElementById(dropdownID), {
    //   placement: "bottom-end"
    // });
    document.getElementById(dropdownID).classList.toggle("hidden");
    document.getElementById(dropdownID).classList.toggle("block");
  }

  function closeMenu(collapseID) {
    console.log(collapseID);
    if (!document.getElementById(collapseID).classList.contains("hidden")) {
      toggleNavbar(collapseID);
    }
  }

  const hamburger_menu = document.querySelector("#hamburger-menu");
  if (hamburger_menu !== null) {
    const observer = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.intersectionRatio !== 1) {
            closeMenu("mobile-menu-sidebar");
          }
        });
      },
      { threshold: 1 }
    );
    observer.observe(hamburger_menu);
  }
});
