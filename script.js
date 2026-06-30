const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const revealItems = document.querySelectorAll(".reveal");

if (reducedMotion) {
  revealItems.forEach((item) => item.classList.add("is-visible"));
} else {
  revealItems.forEach((item, index) => {
    window.setTimeout(() => item.classList.add("is-visible"), 120 + index * 130);
  });
}

const wordElement = document.querySelector(".scribble-word");
const words = wordElement?.dataset.words.split(",") ?? [];
let wordIndex = 0;

if (!reducedMotion && wordElement && words.length > 1) {
  window.setInterval(() => {
    wordElement.classList.add("is-changing");
    window.setTimeout(() => {
      wordIndex = (wordIndex + 1) % words.length;
      wordElement.textContent = words[wordIndex];
      wordElement.classList.remove("is-changing");
    }, 180);
  }, 2600);
}

const tabs = [...document.querySelectorAll(".lens-tab")];
const panels = [...document.querySelectorAll(".lens-panel")];

function activateLens(tab) {
  const lens = tab.dataset.lens;

  tabs.forEach((candidate) => {
    const active = candidate === tab;
    candidate.classList.toggle("is-active", active);
    candidate.setAttribute("aria-selected", String(active));
    candidate.tabIndex = active ? 0 : -1;
  });

  panels.forEach((panel) => {
    const active = panel.dataset.panel === lens;
    panel.hidden = !active;
    panel.classList.toggle("is-active", active);

    if (active && !reducedMotion) {
      panel.classList.remove("is-entering");
      requestAnimationFrame(() => panel.classList.add("is-entering"));
    }
  });
}

tabs.forEach((tab, index) => {
  tab.addEventListener("click", () => activateLens(tab));
  tab.addEventListener("keydown", (event) => {
    if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;

    event.preventDefault();
    let nextIndex = index;

    if (event.key === "ArrowRight") nextIndex = (index + 1) % tabs.length;
    if (event.key === "ArrowLeft") nextIndex = (index - 1 + tabs.length) % tabs.length;
    if (event.key === "Home") nextIndex = 0;
    if (event.key === "End") nextIndex = tabs.length - 1;

    tabs[nextIndex].focus();
    activateLens(tabs[nextIndex]);
  });
});

document.querySelectorAll(".project").forEach((project) => {
  const toggle = project.querySelector(".project-toggle");
  const detail = project.querySelector(".project-detail");
  const startsOpen = project.classList.contains("is-open");

  toggle.setAttribute("aria-expanded", String(startsOpen));
  detail.setAttribute("aria-hidden", String(!startsOpen));

  toggle.addEventListener("click", () => {
    const opening = !project.classList.contains("is-open");

    document.querySelectorAll(".project.is-open").forEach((openProject) => {
      if (openProject !== project) {
        openProject.classList.remove("is-open");
        openProject.querySelector(".project-toggle").setAttribute("aria-expanded", "false");
        openProject.querySelector(".project-detail").setAttribute("aria-hidden", "true");
      }
    });

    project.classList.toggle("is-open", opening);
    toggle.setAttribute("aria-expanded", String(opening));
    detail.setAttribute("aria-hidden", String(!opening));
  });
});

const cursor = document.querySelector(".cursor-dot");

if (cursor && window.matchMedia("(pointer: fine)").matches && !reducedMotion) {
  window.addEventListener("mousemove", (event) => {
    cursor.style.transform = `translate(${event.clientX}px, ${event.clientY}px) translate(-50%, -50%)`;
    cursor.classList.add("is-visible");
  });

  document.querySelectorAll("a, button").forEach((interactive) => {
    interactive.addEventListener("mouseenter", () => cursor.classList.add("is-hovering"));
    interactive.addEventListener("mouseleave", () => cursor.classList.remove("is-hovering"));
  });

  document.documentElement.addEventListener("mouseleave", () => {
    cursor.classList.remove("is-visible");
  });
}

if (!reducedMotion && window.matchMedia("(pointer: fine)").matches) {
  document.querySelectorAll(".magnetic").forEach((element) => {
    element.addEventListener("mousemove", (event) => {
      const rect = element.getBoundingClientRect();
      const x = event.clientX - rect.left - rect.width / 2;
      const y = event.clientY - rect.top - rect.height / 2;
      element.style.transform = `translate(${x * 0.08}px, ${y * 0.08}px)`;
    });

    element.addEventListener("mouseleave", () => {
      element.style.transform = "";
    });
  });
}

const currentYear = document.querySelector("#year");
if (currentYear) currentYear.textContent = new Date().getFullYear();
