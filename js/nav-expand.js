// nav-expand.js — Force all md-nav__item--section toggles to stay checked.
// Material's JS collapses sections via checkbox state; we override that here.
(function () {
  'use strict';

  function expandSections() {
    document.querySelectorAll(
      '.md-nav__item--section > input.md-nav__toggle'
    ).forEach(function (toggle) {
      toggle.checked = true;
    });
  }

  // Run on initial page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', expandSections);
  } else {
    expandSections();
  }

  // Re-run after Material's instant navigation swaps the page
  document.addEventListener('DOMContentLoaded', expandSections);
  document.addEventListener('visibilitychange', expandSections);

  // Hook Material's custom navigation event if available
  if (typeof document$ !== 'undefined') {
    document$.subscribe(expandSections);
  }
})();
