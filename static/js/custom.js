$(document).ready(function() {

    $('.comment_reply_form').hide();

    $('.comment_reply').click(function () {
        $(this).next().show()
    });

    $('.comment_reply_form_cancel').click(function () {
        $('.comment_reply_form').hide();
    });

});