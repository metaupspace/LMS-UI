import glob
import re
import os

files = sorted(glob.glob('designs/admin/code/*.html'))

modified_files = []

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig_content = content
    
    # 1. H1 Page title: 32px / 700 / -0.4px
    # Update .page-head h1 font-size 28px -> 32px (e.g., invite-users.html)
    if fname == 'invite-users.html':
        content = re.sub(
            r'(\.page-head h1\s*\{[^}]*font-size:\s*)28px([^}]*\})',
            r'\1 32px; font-weight:700; letter-spacing:-0.4px; color:var(--text-primary)\2',
            content
        )
    
    # 2. H1 Entity/Detail title: 24px / 700
    if fname == 'user-detail.html':
        content = re.sub(
            r'(\.profile-name\s*\{[^}]*font-size:\s*)22px; font-weight:700; letter-spacing:-\.2px;',
            r'\1 24px; font-weight:700;',
            content
        )
    elif fname == 'integration-detail.html':
        content = re.sub(
            r'(\.header-meta h1\s*\{[^}]*font-size:\s*)22px;',
            r'\1 24px;',
            content
        )
    elif fname == 'role-detail.html':
        content = re.sub(
            r'(\.page-head h1\s*\{[^}]*font-size:\s*)28px; font-weight:700; letter-spacing:-\.3px;',
            r'\1 24px; font-weight:700;',
            content
        )
    elif fname == 'learner-reports.html':
        content = re.sub(
            r'(\.learner-name\s*\{[^}]*font-size:\s*)22px;',
            r'\1 24px;',
            content
        )
    elif fname == 'course-performance-reports.html':
        content = re.sub(
            r'(\.detail-title-row h2\s*\{[^}]*font-size:\s*)22px;',
            r'\1 24px;',
            content
        )

    # 3. H2 Section/Card heading: 18px / 700 / -0.1px
    # Selectors to normalize:
    # .card-header h2, .panel-head h2, .list-card-head h2, .workspace-panel h2, .card-box-title, .table-card-title, .activity-intro h2, .module-title h2, .card h2, .panel-head-title h2
    
    # .card-header h2
    content = re.sub(
        r'(\.card-header h2\s*\{[^}]*font-size:\s*)(?:18px|16\.5px); font-weight:\s*(?:600|700); letter-spacing:\s*-\.?1px;',
        r'\1 18px; font-weight:700; letter-spacing:-0.1px;',
        content
    )
    
    # .panel-head h2
    content = re.sub(
        r'(\.panel-head h2\s*\{[^}]*font-size:\s*)(?:16\.5px|15px); font-weight:\s*(?:600|700);(?: letter-spacing:\s*-\.?15px;)?',
        r'\1 18px; font-weight:700; letter-spacing:-0.1px;',
        content
    )
    
    # .list-card-head h2
    content = re.sub(
        r'(\.list-card-head h2\s*\{[^}]*font-size:\s*)16\.5px; font-weight:700; letter-spacing:-\.15px;',
        r'\1 18px; font-weight:700; letter-spacing:-0.1px;',
        content
    )

    # .workspace-panel h2
    content = re.sub(
        r'(\.workspace-panel h2\s*\{[^}]*font-size:\s*)18px;letter-spacing:-\.15px',
        r'\1 18px; font-weight:700; letter-spacing:-0.1px;',
        content
    )

    # .activity-intro h2
    content = re.sub(
        r'(\.activity-intro h2\s*\{[^}]*font-size:\s*)16px',
        r'\1 18px; font-weight:700; letter-spacing:-0.1px;',
        content
    )

    # .card-box-title
    content = re.sub(
        r'(\.card-box-title\s*\{[^}]*font-size:\s*)16px;',
        r'\1 18px; letter-spacing:-0.1px;',
        content
    )

    # .table-card-title
    content = re.sub(
        r'(\.table-card-title\s*\{[^}]*font-size:\s*)16px;',
        r'\1 18px; letter-spacing:-0.1px;',
        content
    )

    # .module-title h2
    content = re.sub(
        r'(\.module-title h2\s*\{[^}]*font-size:\s*)15\.5px; font-weight:700; letter-spacing:-\.1px;',
        r'\1 18px; font-weight:700; letter-spacing:-0.1px;',
        content
    )

    # .card h2 in user-detail.html
    if fname == 'user-detail.html':
        content = re.sub(
            r'(\.card h2\s*\{[^}]*font-size:\s*)15\.5px; font-weight:700; letter-spacing:-\.1px;',
            r'\1 18px; font-weight:700; letter-spacing:-0.1px;',
            content
        )

    # .panel-head-title h2 in workflow-detail.html
    if fname == 'workflow-detail.html':
        content = re.sub(
            r'(\.panel-head-title h2\s*\{[^}]*font-size:\s*)15px; font-weight:600;',
            r'\1 18px; font-weight:700; letter-spacing:-0.1px;',
            content
        )
        # Fix inline h2 styles in workflow-detail.html
        content = content.replace(
            '<h2 style="font-size:20px; font-weight:700; margin:0 0 4px;">',
            '<h2 style="font-size:18px; font-weight:700; letter-spacing:-0.1px; margin:0 0 4px;">'
        )

    # 4. H3 Modal/Subsection heading: 16px / 700
    # .modal-head h3, .modal-head h2, .drawer-head h3, .modal h3, .modal-title, .certificate-modal h3, .au-head h3, .bi-head h3
    content = re.sub(
        r'(\.modal-head h3\s*\{[^}]*font-size:\s*)(?:17px|18px); font-weight:\s*(?:500|700);',
        r'\1 16px; font-weight:700;',
        content
    )

    content = re.sub(
        r'(\.drawer-head h3\s*\{[^}]*font-size:\s*)17px; font-weight: 700;',
        r'\1 16px; font-weight: 700;',
        content
    )

    content = re.sub(
        r'(\.certificate-modal h3\s*\{[^}]*font-size:\s*)18px',
        r'\1 16px; font-weight:700;',
        content
    )

    content = re.sub(
        r'(\.au-head h3\s*\{[^}]*font-size:\s*)17px; font-weight:700;',
        r'\1 16px; font-weight:700;',
        content
    )

    content = re.sub(
        r'(\.bi-head h3\s*\{[^}]*font-size:\s*)17px; font-weight:700;',
        r'\1 16px; font-weight:700;',
        content
    )

    content = re.sub(
        r'(\.modal-title\s*\{[^}]*font-size:\s*)18px; font-weight:500;',
        r'\1 16px; font-weight:700;',
        content
    )

    if fname in ['workflow-create.html', 'workflow-detail.html', 'workflow-list.html']:
        content = re.sub(
            r'(\.modal-head h2\s*\{[^}]*font-size:\s*)17px; font-weight:700;',
            r'\1 16px; font-weight:700;',
            content
        )

    # 5. H4 Step/Form-group heading: 14px / 700
    # .au-panel h4, .bi-dropzone h4
    content = re.sub(
        r'(\.au-panel h4\s*\{[^}]*font-size:\s*)14\.5px; font-weight:700;',
        r'\1 14px; font-weight:700;',
        content
    )
    content = re.sub(
        r'(\.bi-dropzone h4\s*\{[^}]*font-size:\s*)14\.5px; font-weight:700;',
        r'\1 14px; font-weight:700;',
        content
    )

    # Inline styles on h4 tags:
    # billing-overview.html: <h4 style="margin:0; font-size:15px; font-weight:700;">
    if fname == 'billing-overview.html':
        content = content.replace(
            '<h4 style="margin:0; font-size:15px; font-weight:700;">',
            '<h4 style="margin:0; font-size:14px; font-weight:700;">'
        )
    
    # integration-detail.html: <h4 style="margin:0 0 10px 0; font-size:13.5px; font-weight:700; color:var(--text-primary);">
    if fname == 'integration-detail.html':
        content = content.replace(
            '<h4 style="margin:0 0 10px 0; font-size:13.5px; font-weight:700; color:var(--text-primary);">',
            '<h4 style="margin:0 0 10px 0; font-size:14px; font-weight:700; color:var(--text-primary);">'
        )
    
    # learner-reports.html: <h4 style="margin:0 0 8px 0; font-size:13.5px; font-weight:700; color:var(--text-primary);">
    if fname == 'learner-reports.html':
        content = content.replace(
            '<h4 style="margin:0 0 8px 0; font-size:13.5px; font-weight:700; color:var(--text-primary);">',
            '<h4 style="margin:0 0 8px 0; font-size:14px; font-weight:700; color:var(--text-primary);">'
        )
    
    # user-management.html: <h4 style="margin:0 0 4px; font-size:14.5px; font-weight:700;"> & <h4 style="margin:0 0 12px; font-size:14.5px; font-weight:700;">
    if fname == 'user-management.html':
        content = content.replace(
            '<h4 style="margin:0 0 4px; font-size:14.5px; font-weight:700;">',
            '<h4 style="margin:0 0 4px; font-size:14px; font-weight:700;">'
        )
        content = content.replace(
            '<h4 style="margin:0 0 12px; font-size:14.5px; font-weight:700;">',
            '<h4 style="margin:0 0 12px; font-size:14px; font-weight:700;">'
        )

    if content != orig_content:
        modified_files.append(fname)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f'Modified {len(modified_files)} files:')
for mf in modified_files:
    print(f' - {mf}')
