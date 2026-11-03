import glob

pattern = '''      <a href="#" class="nav-item" title="Settings">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.671 4.136a2.34 2.34 0 0 1 4.659 0 2.34 2.34 0 0 0 3.319 1.915 2.34 2.34 0 0 1 2.33 4.033 2.34 2.34 0 0 0 0 3.831 2.34 2.34 0 0 1-2.33 4.033 2.34 2.34 0 0 0-3.319 1.915 2.34 2.34 0 0 1-4.659 0 2.34 2.34 0 0 0-3.32-1.915 2.34 2.34 0 0 1-2.33-4.033 2.34 2.34 0 0 0 0-3.831A2.34 2.34 0 0 1 6.35 6.051a2.34 2.34 0 0 0 3.319-1.915"/><circle cx="12" cy="12" r="3"/></svg>
        <span>Settings</span>
      </a>
'''

admin_files = glob.glob('designs/admin/code/*.html')
count = 0
for f in admin_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if pattern in content:
        content = content.replace(pattern, '')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1

print(f"Updated {count} admin files.")
