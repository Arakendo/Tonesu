// datatables-init.js
// Adds filter + sort to registry index and english index tables via DataTables 2.x
// DataTables CSS is intentionally not loaded — Material theme styling is used instead.

(function () {
  var TARGETS = [
    /\/tonesu\/registry\/?$/,
    /\/tonesu\/registry\/index\/?$/,
    /\/tonesu\/registry\/english\/?$/,
  ];

  function isTargetPage() {
    return TARGETS.some(function (p) { return p.test(window.location.pathname); });
  }

  function initTables() {
    if (!isTargetPage()) return;
    if (!window.DataTable) return;
    document.querySelectorAll('.md-content__inner table').forEach(function (table) {
      if (!DataTable.isDataTable(table)) {
        new DataTable(table, {
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
  }

  // Hook into Material's SPA navigation observable if available, otherwise DOMContentLoaded
  if (typeof document$ !== 'undefined') {
    document$.subscribe(initTables);
  } else {
    document.addEventListener('DOMContentLoaded', initTables);
  }
})();
