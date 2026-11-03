import glob

pattern = '<a href="#" role="menuitem">My Profile</a>'
replacement = '<a href="profile.html" role="menuitem">My Profile</a>'

admin_files = glob.glob('designs/admin/code/*.html')
count = 0
for f in admin_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if pattern in content:
        content = content.replace(pattern, replacement)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1

print(f"Updated profile link in {count} admin files.")
