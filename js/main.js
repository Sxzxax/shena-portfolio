/* ==========================================================================
   Main script
   ========================================================================== */

// Let CSS know JS is available (used for the nav toggle and reveal effects)
document.documentElement.classList.replace("no-js", "js");

/* ---- Mobile navigation ---- */
const navToggle = document.querySelector(".nav__toggle");
const navList = document.querySelector(".nav__list");

function closeNav() {
  navToggle.setAttribute("aria-expanded", "false");
  navList.classList.remove("is-open");
}

if (navToggle && navList) {
  navToggle.addEventListener("click", () => {
    const isOpen = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!isOpen));
    navList.classList.toggle("is-open", !isOpen);
  });

  // Close the menu after choosing a link
  navList.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeNav();
  });

  // Close with Escape and return focus to the toggle
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && navList.classList.contains("is-open")) {
      closeNav();
      navToggle.focus();
    }
  });
}

/* ---- Light/dark theme toggle ----
   The choice is stored in localStorage; without a choice the site follows the system
   setting. The inline script in <head> applies a saved choice before the page is drawn. */
const themeToggle = document.querySelector("[data-theme-toggle]");
const systemLight = window.matchMedia("(prefers-color-scheme: light)");

function currentTheme() {
  return document.documentElement.dataset.theme || (systemLight.matches ? "light" : "dark");
}

function showTheme() {
  themeToggle.setAttribute("aria-pressed", String(currentTheme() === "light"));
}

if (themeToggle) {
  themeToggle.hidden = false;
  showTheme();

  themeToggle.addEventListener("click", () => {
    const next = currentTheme() === "light" ? "dark" : "light";
    document.documentElement.dataset.theme = next;
    try {
      localStorage.setItem("theme", next);
    } catch (e) {
      // Storage blocked (e.g. private mode): the choice lasts until the page is left
    }
    showTheme();
  });

  // Follow system changes while the visitor hasn't made a choice
  systemLight.addEventListener("change", showTheme);
}

/* ---- Footer year ---- */
document.querySelectorAll("[data-year]").forEach((el) => {
  el.textContent = new Date().getFullYear();
});

/* ---- Sliders (prev/next buttons; without JS the track still scrolls) ---- */
document.querySelectorAll("[data-slider]").forEach((slider) => {
  const track = slider.querySelector("[data-slider-track]");
  const prev = slider.querySelector("[data-slider-prev]");
  const next = slider.querySelector("[data-slider-next]");
  if (!track || !prev || !next) return;

  prev.parentElement.hidden = false;

  const step = () => {
    const item = track.firstElementChild;
    const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
    return item ? item.getBoundingClientRect().width + gap : track.clientWidth;
  };

  const update = () => {
    const max = track.scrollWidth - track.clientWidth;
    prev.disabled = track.scrollLeft <= 1;
    next.disabled = track.scrollLeft >= max - 1;
    // Hide the buttons when everything already fits
    prev.parentElement.hidden = max <= 1;
  };

  const behavior = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth";
  prev.addEventListener("click", () => track.scrollBy({ left: -step(), behavior }));
  next.addEventListener("click", () => track.scrollBy({ left: step(), behavior }));
  track.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  update();
});

/* ---- "Op deze pagina" menu (competentie pages) ----
   A link to a leerdoel (from the menu, the STARR-reflectie or another page) opens its accordion; the section in view is highlighted.
   Without JS the links still jump to each section. */
const toc = document.querySelector("[data-toc]");

function openTarget(hash) {
  const target = hash && document.getElementById(decodeURIComponent(hash.slice(1)));
  if (target && target.tagName === "DETAILS") target.open = true;
}

if (toc) {
  openTarget(location.hash);
  window.addEventListener("hashchange", () => openTarget(location.hash));
  // Any in-page link to a leerdoel (the menu, or the codes in the STARR-reflectie);
  // also when the URL already has that hash, so hashchange doesn't fire
  document.addEventListener("click", (event) => {
    const link = event.target.closest("a[href^='#']");
    if (link) openTarget(link.getAttribute("href"));
  });

  const links = [...toc.querySelectorAll(".toc__item > .toc__link")];
  const sections = links.map((link) => document.getElementById(link.getAttribute("href").slice(1))).filter(Boolean);

  // The current section is the last one whose top has passed a line a third down the screen
  let ticking = false;
  function highlight() {
    ticking = false;
    const line = window.innerHeight / 3;
    const atBottom = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2;
    const current = atBottom
      ? sections[sections.length - 1]
      : sections.filter((section) => section.getBoundingClientRect().top <= line).pop() || sections[0];
    links.forEach((link) => {
      const active = link.getAttribute("href") === `#${current.id}`;
      link.classList.toggle("is-active", active);
      if (active) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  }

  if (sections.length) {
    window.addEventListener("scroll", () => {
      if (!ticking) requestAnimationFrame(highlight);
      ticking = true;
    }, { passive: true });
    highlight();
  }
}

/* ---- Reveal elements on scroll ---- */
const revealItems = document.querySelectorAll(".reveal");
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (!prefersReducedMotion && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}
