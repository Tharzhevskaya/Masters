;
function sendLoginData(url) {
    user_data = {};
    user_data.password = $('#user-password').val();
    user_data.email = $('#user-email').val();
    function onResult(data, status) {
        if (status != "success") {
            $('#auth-status').text("Неверный логин или пароль");
        }
    }
    $.get({
        url: '',
        data: user_data,
        success: onResult
    });
};
function restorePassword(url) {
    user_data = {};
    user_data.email = $('#pwd-email').val();
    $.get({
        url: url,
        data: user_data,
    });
}