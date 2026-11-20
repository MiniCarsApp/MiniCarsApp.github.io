// Light / dark switch. With no choice saved the site follows the system theme;
// a tap picks the opposite of what is shown now and remembers it in this browser.
// The saved choice is applied by a tiny inline script in <head>, before the page
// paints, so there is no flash of the other theme.
(function () {
  var root = document.documentElement;
  var button = document.querySelector(".theme-toggle");
  if (!button) return;
  var systemDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)");

  function isDark() {
    var chosen = root.getAttribute("data-theme");
    if (chosen) return chosen === "dark";
    return !!(systemDark && systemDark.matches);
  }

  function sync() {
    button.setAttribute("aria-pressed", isDark() ? "true" : "false");
  }

  button.addEventListener("click", function () {
    var next = isDark() ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("theme", next); } catch (e) { /* private mode: not remembered */ }
    sync();
  });

  if (systemDark && systemDark.addEventListener) systemDark.addEventListener("change", sync);
  sync();
})();
