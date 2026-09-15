/**
 * 鲲鹏志 · 三更道场 · 页面阅读量与音频播放量边缘计数器客户端
 */
(function () {
  const badge = document.getElementById('page-counter-badge');
  const countEl = document.getElementById('page-views-count');
  if (!badge || !countEl) return;

  const slug = window.location.pathname;

  // 发送阅读计数 POST 请求
  fetch('/api/counter', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ slug: slug, type: 'view' }),
  })
    .then((res) => {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    })
    .then((data) => {
      if (typeof data.count === 'number' && data.count > 0) {
        countEl.textContent = data.count.toLocaleString();
      } else {
        countEl.textContent = '-';
      }
    })
    .catch(() => {
      countEl.textContent = '-';
    });
})();
