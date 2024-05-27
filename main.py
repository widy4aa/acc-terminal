import login_view
import dashboard_view

status_login = login_view.login()

dashboard_view.dashboard(status_login)