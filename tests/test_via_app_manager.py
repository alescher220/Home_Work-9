from app.application import Application


def test_via_app_manager():
    app = Application()

    app.left_panel.open_simple_registration_form()
    app.simple_registration_form\
        .fill_name('ViaAppManager')\
        .submit()\
        .should_have_success_message()
