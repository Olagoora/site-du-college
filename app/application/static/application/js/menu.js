document.addEventListener("DOMContentLoaded", () => {

    const toggles = document.querySelectorAll(".menu-toggle");

    toggles.forEach((toggle) => {

        toggle.addEventListener("click", () => {

            const submenuId = toggle.getAttribute("aria-controls");
            const submenu = document.getElementById(submenuId);

            if (!submenu) {
                return;
            }

            const isOpen = toggle.classList.contains("is-open");

            toggle.classList.toggle("is-open", !isOpen);

            toggle.classList.toggle("is-closed", isOpen);

            toggle.setAttribute(
                "aria-expanded",
                String(!isOpen)
            );

            submenu.classList.toggle(
                "is-open",
                !isOpen
            );

            submenu.setAttribute(
                "aria-hidden",
                String(isOpen)
            );

            const icon = toggle.querySelector(".menu-toggle-icon");

            if (icon) {
                icon.textContent = isOpen ? "+" : "−";
            }

        });

    });

});