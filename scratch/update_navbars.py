import glob
import re

PAGES_INFO = {
    'dashboard.html': {'title': 'Dashboard', 'active': 'dashboard'},
    'user-management.html': {'title': 'User Management', 'active': 'users'},
    'roles.html': {'title': 'Roles & Permissions', 'active': 'roles'},
    'role-detail.html': {'title': 'Role Detail', 'active': 'roles'},
    'user-detail.html': {'title': 'User Detail', 'active': 'users'},
    'workflow-list.html': {'title': 'Workflows', 'active': 'workflows'},
    'workflow-create.html': {'title': 'Create Workflow', 'active': 'workflows'},
    'workflow-detail.html': {'title': 'Workflow Detail', 'active': 'workflows'},
    'certificate-templates.html': {'title': 'Certificates', 'active': 'certificates'},
    'certificates-overview.html': {'title': 'Certificates Overview', 'active': 'certificates'},
    'community-moderation.html': {'title': 'Community Moderation', 'active': 'community'},
    'integrations-catalog.html': {'title': 'Integrations Catalog', 'active': 'integrations'},
    'integration-detail.html': {'title': 'Integration Detail', 'active': 'integrations'},
    'api-webhooks.html': {'title': 'API & Webhooks', 'active': 'integrations'},
    'invite-users.html': {'title': 'Invite Users', 'active': 'users'},
    'learner-reports.html': {'title': 'Learner Reports', 'active': 'reports'},
    'course-performance-reports.html': {'title': 'Course Performance', 'active': 'reports'},
    'concept-mastery-gap-analysis.html': {'title': 'Concept Mastery', 'active': 'reports'},
    'export-custom-reports.html': {'title': 'Export Reports', 'active': 'reports'},
}

NAV_CSS = """  /* Shell Layout — standardized to billing-overview.html */
  .shell { display: grid; grid-template-columns: 232px 1fr; grid-template-rows: 80px 1fr; min-height: 100vh; }

  /* Sidebar */
  .sidebar {
    grid-column: 1; grid-row: 1 / -1;
    background: #ffffff; border-right: 1px solid var(--border-default);
    display: flex; flex-direction: column; overflow-y: auto;
  }
  .sidebar-backdrop {
    display: none; position: fixed; inset: 0; background: rgba(15, 23, 42, 0.45); z-index: 15;
  }
  .sidebar-logo {
    height: 80px; flex-shrink: 0; display: flex; align-items: center;
    padding: 0 20px;
  }
  .brand-link { display: flex; align-items: center; }
  .brand-logo { height: 20px; width: auto; color: var(--text-primary); transition: opacity .15s ease; flex-shrink: 0; }
  .brand-link:hover .brand-logo { opacity: .8; }

  .nav-scroll { padding: 14px 12px 6px; display: flex; flex-direction: column; flex: 1; gap: 2px; }
  .nav-item {
    position: relative; display: flex; align-items: center; gap: 12px; padding: 10px 12px;
    border-radius: var(--radius-lg); color: var(--text-secondary);
    transition: background-color .15s ease, color .15s ease;
  }
  .nav-item span { font-size: 13.5px; font-weight: 600; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; min-width: 0; }
  .nav-item svg { width: 19px; height: 19px; flex-shrink: 0; transition: transform .15s ease; }
  .nav-item:hover { background: var(--surface-raised); color: var(--text-primary); }
  .nav-item:hover svg { transform: translateY(-1px); }
  .nav-item:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: -2px; }
  .nav-item.active { background: var(--info-subtle); color: var(--info); font-weight: 700; }
  .nav-item.active:hover { background: var(--info-subtle); }
  .nav-bottom { margin-top: auto; display: flex; flex-direction: column; gap: 2px; padding: 10px 12px; border-top: 1px solid var(--border-subtle); }
  .nav-item.danger:hover { background: var(--error-subtle); color: var(--error); }

  /* Topbar */
  .topbar {
    grid-column: 2; grid-row: 1;
    display: flex; align-items: center; justify-content: space-between; gap: 16px;
    padding: 0 32px 0 20px; background: #ffffff; border-bottom: 1px solid var(--border-default); z-index: 10;
  }
  .topbar-left { display: flex; align-items: center; gap: 14px; min-width: 0; }
  .breadcrumb { display: flex; align-items: center; gap: 6px; font-size: 13px; min-width: 0; overflow: hidden; }
  .breadcrumb a { color: var(--text-tertiary); font-weight: 600; }
  .breadcrumb a:hover { color: var(--text-primary); }
  .breadcrumb .breadcrumb-sep { color: var(--text-disabled); }
  .breadcrumb .breadcrumb-current { color: var(--text-primary); font-weight: 700; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .topbar-actions { display: flex; align-items: center; gap: 6px; }
  .icon-btn {
    width: 36px; height: 36px; border-radius: 50%; border: none; background: transparent;
    color: var(--text-secondary); display: flex; align-items: center; justify-content: center;
    cursor: pointer; flex-shrink: 0;
  }
  .icon-btn:hover { background: var(--surface-raised); }
  .icon-btn:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 1px; }
  .icon-btn svg { width: 18px; height: 18px; }
  .search-input-wrap { position: relative; width: 240px; }
  .search-input-wrap svg { position: absolute; left: 12px; top: 50%; transform: translateY(-50%); width: 16px; height: 16px; color: var(--icon-muted); pointer-events: none; }
  .search-input-wrap input {
    width: 100%; height: 36px; padding: 0 12px 0 34px; border-radius: var(--radius-lg);
    border: 1px solid var(--border-default); background: var(--surface-raised); font-size: 13px; color: var(--text-primary); outline: none;
  }
  .search-input-wrap input::placeholder { color: var(--text-tertiary); }
  .search-input-wrap input:focus { border-color: var(--focus-ring); }
  .profile-menu { position: relative; flex-shrink: 0; margin-left: 6px; }
  .avatar-btn {
    width: 36px; height: 36px; border-radius: 50%; border: none; cursor: pointer; padding: 0; overflow: hidden;
    background: linear-gradient(135deg, #f59e0b, #dc2626); color: #fff; font-size: 13px; font-weight: 700;
    display: flex; align-items: center; justify-content: center;
  }
  .avatar-btn:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 2px; }
  .profile-dropdown {
    position: absolute; top: 44px; right: 0; width: 200px; background: #ffffff;
    border: 1px solid var(--border-default); border-radius: var(--radius-lg);
    box-shadow: 0 12px 32px -8px rgba(23,23,23,.18); padding: 6px; display: none; z-index: 20;
  }
  .profile-dropdown.show, .profile-dropdown.open { display: block; }
  .profile-dropdown a { display: block; padding: 9px 10px; border-radius: 6px; font-size: 13.5px; color: var(--text-primary); }
  .profile-dropdown a:hover { background: var(--surface-raised); }
  .profile-dropdown hr { border: none; border-top: 1px solid var(--border-subtle); margin: 6px 2px; }
  .profile-dropdown a.danger { color: var(--error); }
"""

NAV_MEDIA_CSS = """  @media (max-width: 960px) {
    .shell { grid-template-columns: 1fr; }
    .topbar { grid-column: 1; padding: 0 20px; }
    .main { grid-column: 1; }
    .sidebar {
      position: fixed; top: 0; left: 0; height: 100vh; width: 240px; z-index: 30;
      transform: translateX(-100%); transition: transform 0.25s ease;
      box-shadow: 4px 0 24px rgba(0,0,0,0.12);
    }
    .sidebar.open { transform: translateX(0); }
    .sidebar-backdrop.show { display: block; }
  }
"""

NAV_JS = """  function toggleProfileDropdown() {
    var d = document.getElementById('profile-dropdown');
    if (d) d.classList.toggle('show');
  }

  function toggleSidebar() {
    var sb = document.querySelector('.sidebar');
    var bd = document.getElementById('sidebarBackdrop');
    if (sb) sb.classList.toggle('open');
    if (bd) bd.classList.toggle('show');
  }
"""

def get_header_html(title):
    return f"""  <header class="topbar">
    <div class="topbar-left">
      <button class="icon-btn" type="button" aria-label="Toggle sidebar" title="Toggle sidebar" onclick="toggleSidebar()">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M15 3v18"/></svg>
      </button>
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="dashboard.html">Admin</a>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-current">{title}</span>
      </nav>
    </div>

    <div class="topbar-actions">
      <div class="search-input-wrap">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21 21-4.34-4.34"/><circle cx="11" cy="11" r="8"/></svg>
        <input type="text" placeholder="Search" aria-label="Search">
      </div>
      <button class="icon-btn" type="button" aria-label="Notifications" title="Notifications">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.268 21a2 2 0 0 0 3.464 0"/><path d="M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326"/></svg>
      </button>
      <div class="profile-menu">
        <button class="avatar-btn" id="profile-btn" type="button" aria-haspopup="true" aria-expanded="false" onclick="toggleProfileDropdown()">AR</button>
        <div class="profile-dropdown" id="profile-dropdown" role="menu">
          <a href="#" role="menuitem">My Profile</a>
          <a href="#" role="menuitem">Account Security</a>
          <a href="#" role="menuitem">Preferences</a>
          <hr>
          <a href="../../Authentication/code/sign-in.html" role="menuitem" class="danger">Log Out</a>
        </div>
      </div>
    </div>
  </header>

  <div class="sidebar-backdrop" id="sidebarBackdrop" onclick="toggleSidebar()"></div>"""

def get_sidebar_html(active_key):
    def is_act(key):
        return ' active' if key == active_key else ''

    return f"""  <nav class="sidebar">
    <div class="sidebar-logo">
      <a href="dashboard.html" class="brand-link" aria-label="UpSpace">
        <svg class="brand-logo" width="140" height="20" viewBox="0 0 148 21" fill="none">
          <g clip-path="url(#brandClip)">
          <path d="M4.29108 16.0632C4.29108 16.5008 4.64765 16.8556 5.0875 16.8556H16.3679C16.8076 16.8556 17.1643 16.5008 17.1643 16.0632V0.792452C17.1643 0.354794 17.5208 0 17.9607 0H20.6588C21.0986 0 21.4552 0.354794 21.4552 0.792452V17.6449C21.4552 18.0826 21.0986 18.4374 20.6588 18.4374H18.0199C17.58 18.4374 17.2235 18.7923 17.2235 19.2298V20.1999C17.2235 20.6376 16.867 20.9924 16.4271 20.9924H5.02774C4.58789 20.9924 4.23133 20.6376 4.23133 20.1999V19.2298C4.23133 18.7923 3.87476 18.4374 3.43491 18.4374H0.796413C0.356566 18.4374 0 18.0826 0 17.6449V0.792452C0 0.354794 0.356566 0 0.796413 0H3.49467C3.93452 0 4.29108 0.354794 4.29108 0.792452V16.0632Z" fill="currentColor"/>
          <path d="M26.6126 20.1964C26.6126 20.6341 26.2561 20.9889 25.8162 20.9889H23.2515C22.8116 20.9889 22.4551 20.6341 22.4551 20.1964V17.2752C22.4551 16.8375 22.8116 16.4827 23.2515 16.4827H25.8162C26.2561 16.4827 26.6126 16.8375 26.6126 17.2752V20.1964ZM38.9092 2.83681C38.9092 3.27447 39.2658 3.62926 39.7056 3.62926H42.2106C42.6505 3.62926 43.007 3.98404 43.007 4.42169L43.0072 7.34296C43.0072 7.78062 42.6505 8.13542 42.2108 8.13542H39.646C39.2062 7.78063 38.8496 7.34297 38.8496 7.34297V5.07899C38.8496 4.64133 38.493 4.28653 38.0532 4.28653H27.409C26.9691 4.28653 26.6126 4.64133 26.6126 5.07899V9.99622C26.6126 10.4339 26.9691 10.7887 27.409 10.7887H38.1128C38.5527 10.7887 38.9092 11.1435 38.9092 11.5811V13.622C38.9092 14.0597 39.2658 14.4144 39.7056 14.4144H42.2106C42.6505 14.4144 43.007 14.7692 43.007 15.2069L43.0072 20.1227C43.0072 20.5603 42.6505 20.9152 42.2108 20.9152H39.646C39.2062 20.9152 38.8496 20.5603 38.8496 20.1227V15.8655C38.8496 15.428 38.493 15.0731 38.0532 15.0731H27.3816C26.9417 15.0731 26.5851 14.7183 26.5851 14.2806V12.4735C26.5851 12.0359 26.2286 11.6811 25.7887 11.6811H23.2515C22.8116 11.6811 22.4551 11.3263 22.4551 10.8886V4.42145C22.4551 3.98379 22.8116 3.629 23.2515 3.629H25.7887C26.2286 3.629 26.5851 3.2742 26.5851 2.83654V0.794406C26.5851 0.356746 26.9417 0.00195312 27.3816 0.00195312H38.1128C38.5527 0.00195312 38.9092 0.356746 38.9092 0.794406V2.83681Z" fill="currentColor"/>
          <path d="M51.0852 15.8278V14.4582H49.6602V5.37032H51.7168V13.6364H55.3765V5.37032H57.4493V14.4582H56.0081V15.8278H51.0852ZM59.0695 15.6506V5.48074H63.2746C63.917 5.48074 64.4815 5.61149 64.9683 5.873C65.4647 6.12483 65.8491 6.48319 66.1217 6.9481C66.4039 7.413 66.5452 7.96508 66.5452 8.60433V8.80772C66.5452 9.43729 66.3992 9.98936 66.1071 10.4639C65.8248 10.9289 65.4355 11.2921 64.9391 11.5536C64.4523 11.8054 63.8975 11.9313 63.2746 11.9313H60.9968V15.6506H59.0695ZM60.9968 10.1879H63.0848C63.5422 10.1879 63.9121 10.062 64.1944 9.81017C64.4766 9.55836 64.6178 9.21451 64.6178 8.77866V8.63338C64.6178 8.19753 64.4766 7.8537 64.1944 7.60187C63.9121 7.35006 63.5422 7.22414 63.0848 7.22414H60.9968V10.1879ZM71.1373 15.8539C70.3488 15.8539 69.6529 15.7136 69.0493 15.4326C68.4459 15.1517 67.9738 14.7498 67.6331 14.2268C67.2925 13.7038 67.122 13.0742 67.122 12.3381V11.9313H69.0201V11.9313C69.0201 12.9483 69.21 13.4083 69.5896 13.7183C69.9692 14.0185 70.4851 14.1687 71.1373 14.1687C71.7992 14.1687 72.2907 14.0379 72.612 13.7764C72.943 13.5149 73.1084 13.1807 73.1084 12.7739C73.1084 12.4931 73.0257 12.2655 72.8602 12.0911C72.7045 11.9168 72.4709 11.7763 72.1593 11.6698C71.8576 11.5536 71.4877 11.447 70.0497 11.3502L70.7139 11.2775C70.013 11.1226 69.4096 10.9289 68.9033 10.6964C68.4069 10.4543 68.0225 10.1395 67.7499 9.75206C67.4871 9.36464 67.3556 8.861 67.3556 8.24112C67.3556 7.62125 67.5017 7.09338 67.7937 6.65753C68.0955 6.212 68.514 5.873 69.0493 5.64055C69.5945 5.39842 70.232 5.27734 70.9621 5.27734C71.6921 5.27734 72.3395 5.40326 72.904 5.65508C73.4783 5.89723 73.926 6.26527 74.2473 6.75923C74.5783 7.24351 74.7437 7.8537 74.7437 8.5898V9.02565H72.8456V8.5898C72.8456 8.20238 72.7678 7.89244 72.612 7.65999C72.466 7.41785 72.2519 7.24351 71.9695 7.13697C71.6873 7.02074 71.3515 6.96263 70.9621 6.96263C70.378 6.96263 69.9449 7.07402 69.6626 7.29678C69.3901 7.50987 69.2538 7.80527 69.2538 8.183C69.2538 8.43483 69.3171 8.64791 69.4436 8.82225C69.5799 8.99659 69.7794 9.14187 70.0422 9.2581C70.305 9.37432 70.6408 9.47602 71.0497 9.56319L71.3855 9.63583C72.1155 9.79081 72.7483 9.98936 73.2836 10.2315C73.8288 10.4736 74.2522 10.7933 74.5539 11.1904C74.8557 11.5875 75.0065 12.096 75.0065 12.7158C75.0065 13.3357 74.8459 13.883 74.5247 14.3575C72.2133 14.8224 73.7654 15.1905 73.1814 15.4617C72.6072 15.7232 71.9257 15.8539 71.1373 15.8539ZM76.1519 15.6506V5.48074H80.3569C80.9994 5.48074 81.564 5.61149 82.0507 5.873C82.5471 6.12483 82.9316 6.48319 83.2041 6.9481C83.4865 7.413 83.6275 7.96508 83.6275 8.60433V8.80772C83.6275 9.43729 83.4815 9.98936 83.1895 10.4639C82.9073 10.9289 82.5179 11.2921 82.0214 11.5536C81.5348 11.8054 80.98 11.9313 80.3569 11.9313H78.0792V15.6506H76.1519ZM78.0792 10.1879H80.1671C80.6247 10.1879 80.9946 10.062 81.2768 9.81017C81.5591 9.55836 81.7002 9.21451 81.7002 8.77866V8.63338C81.7002 8.19753 81.5591 7.8537 81.2768 7.60187C80.9946 7.35006 80.6247 7.22414 80.1671 7.22414H78.0792V10.1879ZM83.1867 15.6506L85.8733 5.48074H89.2315L91.9181 15.6506H89.9323L89.3775 13.4132H85.7273L85.1725 15.6506H83.1867ZM86.1799 11.6407H88.9249L87.6838 6.68659H87.421L86.1799 11.6407ZM96.6477 15.8539C95.3823 15.8539 94.3796 15.5053 93.6399 14.8079C92.9002 14.1009 92.5302 13.0936 92.5302 11.786V9.34527C92.5302 8.03772 92.9002 7.03527 93.6399 6.33791C94.3796 5.63087 95.3823 5.27734 96.6477 5.27734C97.9034 5.27734 98.8719 5.62119 99.5533 6.30885C100.244 6.98685 100.59 7.92149 100.59 9.11282V9.19998H98.6918V9.0547C98.6918 8.45421 98.5215 7.96025 98.1808 7.57282C97.8499 7.1854 97.3389 6.99168 96.6477 6.99168C95.9664 6.99168 95.4309 7.19993 95.0416 7.6164C94.6523 8.03289 94.4576 8.59949 94.4576 9.31621V11.8151C94.4576 12.5221 94.6523 13.0887 95.0416 13.5149C95.4309 13.9313 95.9664 14.1396 96.6477 14.1396C97.3389 14.1396 97.8499 13.9459 98.1808 13.5585C98.5215 13.1614 98.6918 12.6674 98.6918 12.0766V11.8151H100.59V12.0185C100.59 13.2098 100.244 14.1492 99.5533 14.837C98.8719 15.5149 97.9034 15.8539 96.6477 15.8539ZM101.868 15.6506V5.48074H108.439V7.22414H103.796V9.65036H108.03V11.3938H103.796V13.9072H108.526V15.6506H101.868ZM113.076 15.6506V5.48074H115.004V13.9072H119.676V15.6506H113.076ZM119.997 15.6506L122.683 5.48074H126.042L128.728 15.6506H126.743L126.188 13.4132H122.537L121.983 15.6506H119.997ZM122.99 11.6407H125.735L124.494 6.68659H124.231L122.99 11.6407ZM129.368 15.6506V13.9653H130.711V7.16602H129.368V5.48074H134.623C135.247 5.48074 135.788 5.58729 136.244 5.80036C136.711 6.00376 137.072 6.29917 137.325 6.68659C137.587 7.06433 137.719 7.51955 137.719 8.05225V8.19753C137.719 8.66244 137.631 9.04502 137.456 9.34527C137.281 9.63583 137.072 9.86345 136.828 10.0281C136.595 10.1831 136.372 10.2945 136.157 10.3622V10.6238C136.372 10.6819 136.605 10.7933 136.857 10.9579C137.111 11.1129 137.325 11.3405 137.5 11.6407C137.686 11.941 137.777 12.3333 137.777 12.8175V12.9628C137.777 13.5245 137.646 14.0089 137.383 14.4156C137.12 14.8128 136.755 15.1179 136.288 15.3309C135.831 15.544 135.295 15.6506 134.682 15.6506H129.368ZM132.638 13.9072H134.448C134.868 13.9072 135.203 13.8055 135.456 13.6021C135.718 13.3987 135.85 13.1081 135.85 12.7304V12.5851C135.85 12.2073 135.724 11.9168 135.47 11.7134C135.218 11.51 134.877 11.4083 134.448 11.4083H132.638V13.9072ZM132.638 9.66489H134.419C134.819 9.66489 135.145 9.56319 135.397 9.3598C135.66 9.1564 135.792 8.87553 135.792 8.51715V8.37187C135.792 8.00383 135.665 7.72295 135.412 7.52923C135.16 7.32583 134.828 7.22414 134.419 7.22414H132.638V9.66489ZM140.513 15.8278V14.4582H139.087V12.2507H141.145V13.6364H144.804V11.6867H140.513V10.3171H139.087V6.75606H140.513V5.37032H145.436V6.75606H146.876V8.94746H144.804V7.57783H141.145V9.51142H145.436V10.8649H146.876V14.4582H145.436V15.8278H140.513Z" fill="currentColor"/>
          </g>
          <defs><clipPath id="brandClip"><rect width="148" height="21" fill="white"/></clipPath></defs>
        </svg>
      </a>
    </div>
    <div class="nav-scroll">
      <a href="dashboard.html" class="nav-item{is_act('dashboard')}" title="Admin Dashboard">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/></svg>
        <span>Dashboard</span>
      </a>
      <a href="user-management.html" class="nav-item{is_act('users')}" title="User Management">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><path d="M16 3.128a4 4 0 0 1 0 7.744"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><circle cx="9" cy="7" r="4"/></svg>
        <span>User Management</span>
      </a>
      <a href="roles.html" class="nav-item{is_act('roles')}" title="Roles &amp; Permissions">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg>
        <span>Roles &amp; Permissions</span>
      </a>
      <a href="#" class="nav-item{is_act('org')}" title="Organization">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 12h4"/><path d="M10 8h4"/><path d="M14 21v-3a2 2 0 0 0-4 0v3"/><path d="M6 10H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-2"/><path d="M6 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16"/></svg>
        <span>Organization</span>
      </a>
      <a href="workflow-list.html" class="nav-item{is_act('workflows')}" title="Workflows">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg>
        <span>Workflows</span>
      </a>
      <a href="certificate-templates.html" class="nav-item{is_act('certificates')}" title="Certificates">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"/><circle cx="12" cy="8" r="6"/></svg>
        <span>Certificates</span>
      </a>
      <a href="community-moderation.html" class="nav-item{is_act('community')}" title="Community">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 17a2 2 0 0 1-2 2H6.828a2 2 0 0 0-1.414.586l-2.202 2.202A.71.71 0 0 1 2 21.286V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2z"/></svg>
        <span>Community</span>
      </a>
      <a href="integrations-catalog.html" class="nav-item{is_act('integrations')}" title="Integrations">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15.39 4.39a1 1 0 0 0 1.68-.474 2.5 2.5 0 1 1 3.014 3.015 1 1 0 0 0-.474 1.68l1.683 1.682a2.414 2.414 0 0 1 0 3.414L19.61 15.39a1 1 0 0 1-1.68-.474 2.5 2.5 0 1 0-3.014 3.015 1 1 0 0 1 .474 1.68l-1.683 1.682a2.414 2.414 0 0 1-3.414 0L8.61 19.61a1 1 0 0 0-1.68.474 2.5 2.5 0 1 1-3.014-3.015 1 1 0 0 0 .474-1.68l-1.683-1.682a2.414 2.414 0 0 1 0-3.414L4.39 8.61a1 1 0 0 1 1.68.474 2.5 2.5 0 1 0 3.014-3.015 1 1 0 0 1-.474-1.68l1.683-1.682a2.414 2.414 0 0 1 3.414 0z"/></svg>
        <span>Integrations</span>
      </a>
      <a href="billing-overview.html" class="nav-item{is_act('billing')}" title="Billing">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/></svg>
        <span>Billing</span>
      </a>
      <a href="learner-reports.html" class="nav-item{is_act('reports')}" title="Reports">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>
        <span>Reports</span>
      </a>
    </div>

    <div class="nav-bottom">
      <a href="#" class="nav-item" title="Settings">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.671 4.136a2.34 2.34 0 0 1 4.659 0 2.34 2.34 0 0 0 3.319 1.915 2.34 2.34 0 0 1 2.33 4.033 2.34 2.34 0 0 0 0 3.831 2.34 2.34 0 0 1-2.33 4.033 2.34 2.34 0 0 0-3.319 1.915 2.34 2.34 0 0 1-4.659 0 2.34 2.34 0 0 0-3.32-1.915 2.34 2.34 0 0 1-2.33-4.033 2.34 2.34 0 0 0 0-3.831A2.34 2.34 0 0 1 6.35 6.051a2.34 2.34 0 0 0 3.319-1.915"/><circle cx="12" cy="12" r="3"/></svg>
        <span>Settings</span>
      </a>
      <a href="../../Authentication/code/sign-in.html" class="nav-item danger" title="Logout">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 17 5-5-5-5"/><path d="M21 12H9"/><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/></svg>
        <span>Logout</span>
      </a>
    </div>
  </nav>"""

def process_file(fn, info):
    filepath = f'designs/admin/code/{fn}'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS
    if '/* Shell Layout — standardized to billing-overview.html */' not in content:
        # replace old shell/sidebar/header css if present
        content = re.sub(r'/\* -+ (?:Header|Sidebar|Shell)[^\n]*\n.*?(?=\/\* -+ [A-Z]|\n  \.(?:main|card|page|btn|kpi))', '', content, flags=re.DOTALL)
        content = content.replace('</style>', f'\n{NAV_CSS}\n{NAV_MEDIA_CSS}\n</style>')

    # 2. Update HTML markup between <div class="shell"> and <main ...> or <div class="main">
    new_topbar = get_header_html(info['title'])
    new_sidebar = get_sidebar_html(info['active'])
    new_header_sidebar_block = f"{new_topbar}\n\n  {new_sidebar}"

    # Match anything inside <div class="shell"> up to <main or <div class="main"
    def replace_header_sidebar(m):
        shell_open = m.group(1)
        main_open = m.group(3)
        return f"{shell_open}\n\n{new_header_sidebar_block}\n\n  {main_open}"

    content = re.sub(
        r'(<div class="shell">\s*)(.*?)(<(?:main|div class="main"))',
        replace_header_sidebar,
        content,
        flags=re.DOTALL
    )

    # 3. Ensure toggleProfileDropdown and toggleSidebar are present in JS
    if 'function toggleSidebar()' not in content:
        content = content.replace('</script>', f'\n{NAV_JS}\n</script>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Processed {fn}')

for fn, info in PAGES_INFO.items():
    process_file(fn, info)
