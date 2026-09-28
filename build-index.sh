#!/usr/bin/env bash
# Regenerates index.html: links to every designs/<section>/code/*.html page.
# Run from repo root after adding/removing pages: bash build-index.sh
set -euo pipefail
cd "$(dirname "$0")"

{
cat <<'EOF'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>UpSpace LMS Designs</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  body { margin: 0; font-family: "DM Sans", system-ui, sans-serif; background: #fafafa; color: #171717; }
  main { max-width: 1100px; margin: 0 auto; padding: 32px 16px 64px; }
  h1 { font-size: 24px; margin: 0 0 4px; }
  p.sub { color: #525252; margin: 0 0 20px; }
  input { width: 100%; box-sizing: border-box; padding: 10px 12px; font: inherit; border: 1px solid #e5e5e5; border-radius: 8px; background: #fff; margin-bottom: 24px; }
  input:focus { outline: 2px solid #6366f1; outline-offset: 1px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
  section { background: #fff; border: 1px solid #e5e5e5; border-radius: 12px; padding: 16px 20px; }
  h2 { font-size: 16px; margin: 0 0 10px; display: flex; justify-content: space-between; }
  h2 span { color: #a3a3a3; font-weight: 500; }
  ul { list-style: none; margin: 0; padding: 0; }
  li a { display: block; padding: 5px 0; color: #4f46e5; text-decoration: none; }
  li a:hover { color: #4338ca; text-decoration: underline; }
  [hidden] { display: none !important; }
</style>
</head>
<body>
<main>
<h1>UpSpace LMS Designs</h1>
<p class="sub">Every design page, grouped by section.</p>
<input id="q" type="search" placeholder="Filter pages…" aria-label="Filter pages">
<div class="grid">
EOF

for dir in designs/*/code; do
  section=$(basename "$(dirname "$dir")")
  files=("$dir"/*.html)
  [ -e "${files[0]}" ] || continue
  echo "<section><h2>${section} <span>${#files[@]}</span></h2><ul>"
  for f in "${files[@]}"; do
    name=$(basename "$f" .html)
    label=$(echo "${name//-/ }" | sed 's/^./\U&/')
    echo "<li><a href=\"$f\">$label</a></li>"
  done
  echo "</ul></section>"
done

cat <<'EOF'
</div>
</main>
<script>
  const q = document.getElementById('q');
  q.addEventListener('input', () => {
    const t = q.value.trim().toLowerCase();
    document.querySelectorAll('section').forEach(s => {
      let shown = 0;
      s.querySelectorAll('li').forEach(li => {
        const hit = !t || (s.querySelector('h2').textContent + ' ' + li.textContent).toLowerCase().includes(t);
        li.hidden = !hit; shown += hit;
      });
      s.hidden = !shown;
    });
  });
</script>
</body>
</html>
EOF
} > index.html
