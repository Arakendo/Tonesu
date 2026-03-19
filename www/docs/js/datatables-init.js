// datatables-init.js
// Adds filter + sort to registry tables via DataTables 2.x
// DataTables CSS is intentionally not loaded — Material theme styling is used instead.

(function () {
  var TARGETS = [
    /\/tonesu\/registry\/?$/,
    /\/tonesu\/registry\/index\/?$/,
    /\/tonesu\/registry\/overview\/?$/,
    /\/tonesu\/registry\/english\/?$/,
  ];

  function isTargetPage() {
    return TARGETS.some(function (p) { return p.test(window.location.pathname); });
  }

  function initTables() {
    if (!isTargetPage()) return;
    if (!window.DataTable) return;
    try {
      document.querySelectorAll('.md-content__inner table').forEach(function (table) {
        if (!window.DataTable.isDataTable(table)) {
          new window.DataTable(table, {
            paging: false,
            info: false,
            layout: {
              topStart: { search: { placeholder: 'Filter…' } },
              topEnd: null,
              bottomStart: null,
              bottomEnd: null,
            },
          });
        }
      });
    } catch (e) {
      console.error('[datatables-init]', e);
    }
  }

  // Material SPA observable — fires on initial load and each navigation
  if (typeof document$ !== 'undefined' && document$ && typeof document$.subscribe === 'function') {
    document$.subscribe(function () { setTimeout(initTables, 0); });
  }

  // Also handle direct page loads where document$ may not replay
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTables);
  } else {
    // DOM already parsed — run immediately
    initTables();
  }
})();
