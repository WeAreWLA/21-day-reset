// WLA social-proof notification widget
// Usage on a page:
//   <script>window.WLA_NOTIFICATIONS = { offer: '21 Day Reset' };</script>
//   <script src="/assets/notifications.js"></script>
//
// Optional config keys:
//   offer     (string)   — what each customer "joined". Default: '21 Day Reset'.
//   customers (string[]) — override the default 30-name list.
//   firstDelay (ms)      — delay before first toast. Default: 5000.
//   showFor   (ms)       — how long each toast stays visible. Default: 6000.
//   gapMin/gapMax (ms)   — random gap between toasts. Default: 12000–30000.
//   position  ('bottom-left'|'bottom-right'). Default: 'bottom-left'.

(function () {
  if (window.__WLA_NOTIFICATIONS_LOADED) return;
  window.__WLA_NOTIFICATIONS_LOADED = true;

  var cfg = window.WLA_NOTIFICATIONS || {};
  var offer = cfg.offer || '21 Day Reset';
  var customers = (cfg.customers && cfg.customers.length) ? cfg.customers : [
    'Ruth H.', 'Sarah M.', 'Vicky T.', 'Laura B.', 'Lisa P.',
    'Barbara F.', 'Tara K.', 'Lucy W.', 'Jenny T.', 'Carol N.',
    'Margaret S.', 'Helen J.', 'Karen D.', 'Susan L.', 'Joan B.',
    'Pauline R.', 'Diane C.', 'Tracey H.', 'Beverley M.', 'Linda P.',
    'Christine A.', 'Maureen S.', 'Patricia W.', 'Gail B.', 'Sandra T.',
    'Janet F.', 'Yvonne K.', 'Hazel R.', 'Brenda L.', 'Wendy O.',
  ];
  var firstDelay = cfg.firstDelay || 5000;
  var showFor = cfg.showFor || 6000;
  var gapMin = cfg.gapMin || 12000;
  var gapMax = cfg.gapMax || 30000;
  var position = cfg.position || 'bottom-left';

  // ─── styles ─────────────────────────────────────────────────────────────
  var css = ''
    + '.wla-notif{position:fixed;bottom:20px;' + (position === 'bottom-right' ? 'right:20px;' : 'left:20px;') + 'max-width:320px;z-index:9999;'
    + 'background:#fff;border:1px solid rgba(14,39,70,0.08);border-radius:12px;'
    + 'padding:14px 36px 14px 14px;display:flex;align-items:center;gap:12px;'
    + 'box-shadow:0 18px 40px -14px rgba(14,39,70,0.28);'
    + 'transform:translate' + (position === 'bottom-right' ? 'X(380px)' : 'X(-380px)') + ';opacity:0;'
    + 'transition:transform .4s ease,opacity .4s ease;'
    + 'font-family:"Alegreya Sans",-apple-system,system-ui,sans-serif;'
    + 'font-size:13px;color:#333;line-height:1.4;}'
    + '.wla-notif.show{transform:translateX(0);opacity:1;}'
    + '.wla-notif-icon{flex:0 0 40px;width:40px;height:40px;border-radius:50%;'
    + 'background:#E87F63;color:#fff;display:flex;align-items:center;justify-content:center;}'
    + '.wla-notif-icon svg{width:20px;height:20px;}'
    + '.wla-notif-body{flex:1;min-width:0;}'
    + '.wla-notif-name{font-weight:700;color:#0e2746;}'
    + '.wla-notif-time{color:#888;font-size:11px;margin-top:3px;letter-spacing:0.02em;}'
    + '.wla-notif-close{position:absolute;top:6px;right:8px;cursor:pointer;color:#bbb;'
    + 'background:none;border:none;font-size:18px;line-height:1;padding:4px;}'
    + '.wla-notif-close:hover{color:#333;}'
    + '@media (max-width:480px){.wla-notif{left:12px;right:12px;max-width:none;bottom:14px;padding:12px 32px 12px 12px;}}';

  var styleEl = document.createElement('style');
  styleEl.textContent = css;
  document.head.appendChild(styleEl);

  // Shopping-bag SVG (Lucide-style)
  var bagSvg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    + '<path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/>'
    + '<line x1="3" y1="6" x2="21" y2="6"/>'
    + '<path d="M16 10a4 4 0 0 1-8 0"/></svg>';

  // ─── helpers ────────────────────────────────────────────────────────────
  function pluralize(n, word) { return n + ' ' + word + (n === 1 ? '' : 's') + ' ago'; }
  function timeAgo(mins) {
    if (mins < 60) return pluralize(Math.max(1, mins), 'min');
    var hrs = Math.floor(mins / 60);
    if (hrs < 24) return pluralize(hrs, 'hour');
    return pluralize(Math.floor(hrs / 24), 'day');
  }
  // Weighted: 60% within last 2h, 40% within last 48h.
  function randomMinutesAgo() {
    if (Math.random() < 0.6) return 2 + Math.floor(Math.random() * 118);          // 2–120 mins
    return 121 + Math.floor(Math.random() * (48 * 60 - 121));                       // 2–48 hours
  }
  function randomGap() { return gapMin + Math.floor(Math.random() * (gapMax - gapMin)); }

  // Pull customers without immediate repeats.
  var queue = [];
  function nextCustomer() {
    if (queue.length === 0) {
      queue = customers.slice().sort(function () { return Math.random() - 0.5; });
    }
    return queue.shift();
  }

  // ─── render ─────────────────────────────────────────────────────────────
  var el = document.createElement('div');
  el.className = 'wla-notif';
  el.setAttribute('role', 'status');
  el.setAttribute('aria-live', 'polite');
  el.innerHTML = ''
    + '<div class="wla-notif-icon">' + bagSvg + '</div>'
    + '<div class="wla-notif-body">'
    +   '<div><span class="wla-notif-name"></span> <span class="wla-notif-action"></span></div>'
    +   '<div class="wla-notif-time"></div>'
    + '</div>'
    + '<button class="wla-notif-close" aria-label="Dismiss">×</button>';

  function attach() { document.body.appendChild(el); }
  if (document.body) attach();
  else document.addEventListener('DOMContentLoaded', attach);

  var nameEl = el.querySelector('.wla-notif-name');
  var actionEl = el.querySelector('.wla-notif-action');
  var timeEl = el.querySelector('.wla-notif-time');
  var closeBtn = el.querySelector('.wla-notif-close');

  var hideTimer, nextTimer, dismissed = false;

  function show() {
    if (dismissed) return;
    var name = nextCustomer();
    nameEl.textContent = name;
    actionEl.textContent = 'joined the ' + offer;
    timeEl.textContent = timeAgo(randomMinutesAgo());
    el.classList.add('show');
    hideTimer = setTimeout(hide, showFor);
  }
  function hide() {
    el.classList.remove('show');
    clearTimeout(hideTimer);
    if (!dismissed) nextTimer = setTimeout(show, randomGap());
  }
  closeBtn.addEventListener('click', function () {
    dismissed = true;
    clearTimeout(hideTimer);
    clearTimeout(nextTimer);
    el.classList.remove('show');
  });

  setTimeout(show, firstDelay);
})();
