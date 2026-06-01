const MENU = [{"label": "🏠 Trang chủ", "href": ""}, {"label": "🚀 Bắt đầu", "href": "quick-start/"}, {"label": "📚 Giáo trình", "children": [{"label": "📖 00. Triết lý", "href": "00-triet-ly/01-tai-sao-ai-first-wiki/"}, {"label": "⚙️ 01. Cài đặt", "href": "01-cai-dat/01-cai-obsidian/"}, {"label": "🧠 02. Kho đầu tiên (Brain)", "href": "02-vault-dau-tien-brain/01-tao-vault-brain/"}, {"label": "🌳 03. Mở rộng multi-vault", "href": "03-mo-rong-multi-vault/01-khi-nao-tach-vault/"}, {"label": "🤖 04. Agents · Skills · Memory", "href": "04-agents-skills-memory/01-agent-la-gi/"}, {"label": "🛠️ 05. Bảo trì", "href": "05-bao-tri-lint/01-lint-wiki-dinh-ky/"}]}, {"label": "📋 Templates", "children": [{"label": "CLAUDE.md master template", "href": "99-templates/claude-md-master-template/"}, {"label": "Concept page template", "href": "99-templates/concept-page-template/"}, {"label": "Course bản đồ nội dung template", "href": "99-templates/course-moc-template/"}, {"label": "index.md format", "href": "99-templates/index-md-format/"}, {"label": "log.md format", "href": "99-templates/log-md-format/"}, {"label": "Source page template", "href": "99-templates/source-page-template/"}]}, {"label": "❓ FAQ", "href": "faq/"}];
(function () {
  function root() {
    var l = document.querySelector('.md-header .md-logo') || document.querySelector('a.md-logo');
    return l ? l.href : (location.origin + '/');
  }
  function build() {
    var header = document.querySelector('.md-header');
    if (!header || document.querySelector('.tm-bar')) return;
    var base = root();
    var bar = document.createElement('nav'); bar.className = 'tm-bar';
    var inner = document.createElement('div'); inner.className = 'tm-inner';
    MENU.forEach(function (item) {
      var wrap = document.createElement('div');
      wrap.className = 'tm-item' + (item.children ? ' tm-has' : '');
      var a = document.createElement('a'); a.className = 'tm-link';
      a.textContent = item.label + (item.children ? '  ▾' : '');
      a.href = new URL(item.href || '', base).href;
      if (item.children) {
        a.addEventListener('click', function (e) {
          if (window.matchMedia('(max-width: 76.1875em)').matches) { e.preventDefault(); wrap.classList.toggle('tm-open'); }
        });
      }
      wrap.appendChild(a);
      if (item.children) {
        var drop = document.createElement('div'); drop.className = 'tm-drop';
        item.children.forEach(function (c) {
          var ca = document.createElement('a');
          ca.href = new URL(c.href, base).href; ca.textContent = c.label;
          drop.appendChild(ca);
        });
        wrap.appendChild(drop);
      }
      inner.appendChild(wrap);
    });
    bar.appendChild(inner);
    header.insertAdjacentElement('afterend', bar);
  }
  if (document.readyState !== 'loading') build();
  else document.addEventListener('DOMContentLoaded', build);
})();
