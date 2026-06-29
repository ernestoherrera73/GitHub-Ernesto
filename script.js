/* Portafolio — interacción ligera: menú móvil, idioma ES/EN, año. */
(function () {
  "use strict";

  /* ---------- Año en el footer ---------- */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ---------- Menú móvil ---------- */
  var burger = document.getElementById("navBurger");
  var navLinks = document.getElementById("navLinks");

  function closeMenu() {
    if (!navLinks) return;
    navLinks.classList.remove("open");
    if (burger) burger.setAttribute("aria-expanded", "false");
  }

  if (burger && navLinks) {
    burger.addEventListener("click", function () {
      var isOpen = navLinks.classList.toggle("open");
      burger.setAttribute("aria-expanded", String(isOpen));
    });
    // Cerrar al hacer clic en un enlace (no en el botón de idioma)
    navLinks.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeMenu);
    });
  }

  /* ---------- Toggle de idioma ES / EN ---------- */
  var langToggle = document.getElementById("langToggle");
  var current = "es";

  function applyLang(lang) {
    var nodes = document.querySelectorAll("[data-es][data-en]");
    nodes.forEach(function (node) {
      var value = lang === "en" ? node.getAttribute("data-en") : node.getAttribute("data-es");
      if (value != null) node.innerHTML = value;
    });
    document.documentElement.lang = lang;
    if (langToggle) {
      // El botón muestra el idioma al que se cambiará
      langToggle.textContent = lang === "en" ? "ES" : "EN";
    }
    current = lang;
    try { localStorage.setItem("preferredLang", lang); } catch (e) {}
  }

  if (langToggle) {
    langToggle.addEventListener("click", function () {
      applyLang(current === "es" ? "en" : "es");
    });
  }

  // Idioma inicial: preferencia guardada > navegador > español
  var initial = "es";
  try {
    var saved = localStorage.getItem("preferredLang");
    if (saved === "es" || saved === "en") {
      initial = saved;
    } else if ((navigator.language || "").toLowerCase().indexOf("en") === 0) {
      initial = "en";
    }
  } catch (e) {}
  if (initial !== "es") applyLang(initial);
  else if (langToggle) langToggle.textContent = "EN";
})();
