(function() {
  function initFootnotePopovers() {
    document.querySelectorAll('.fn-btn').forEach(function(btn) {
      btn.onclick = function(e) {
        e.preventDefault();
        e.stopPropagation();
        var targetId = btn.getAttribute('data-fn-id');
        var popover = document.getElementById(targetId);
        document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) {
          if (p.id !== targetId) p.classList.add('hidden');
        });
        if (popover && popover.classList.contains('hidden')) {
          var rect = btn.getBoundingClientRect();
          var scrollY = window.scrollY;
          var top = rect.bottom + scrollY + 8;
          var left = rect.left;
          if (left + 320 > window.innerWidth) left = window.innerWidth - 340;
          if (left < 20) left = 20;
          popover.style.top = top + 'px';
          popover.style.left = left + 'px';
          popover.classList.remove('hidden');
        } else if (popover) {
          popover.classList.add('hidden');
        }
      };
    });
    document.querySelectorAll('.mobile-fn-btn').forEach(function(btn) {
      btn.onclick = function(e) {
        e.preventDefault();
        e.stopPropagation();
        var targetId = btn.getAttribute('data-fn-id');
        var popover = document.getElementById(targetId);
        document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) {
          if (p.id !== targetId) p.classList.add('hidden');
        });
        if (popover) popover.classList.toggle('hidden');
      };
    });
    document.querySelectorAll('.fn-close').forEach(function(btn) {
      btn.onclick = function(e) {
        e.preventDefault();
        e.stopPropagation();
        var popover = btn.closest('.fn-popover, .fn-popover-mobile');
        if (popover) popover.classList.add('hidden');
      };
    });
  }
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.fn-popover') && !e.target.closest('.fn-popover-mobile') && !e.target.closest('.fn-btn') && !e.target.closest('.mobile-fn-btn')) {
      document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) { p.classList.add('hidden'); });
    }
  });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) { p.classList.add('hidden'); });
    }
  });
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initFootnotePopovers);
  } else {
    initFootnotePopovers();
  }
})();
