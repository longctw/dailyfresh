$(function(){

    $('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$("#lg_form").submit(function(){
        if (check_user_name() && check_pwd()){
            return true;
        }else{
            return false;
        }
    });

})

function check_user_name(){
    var len = $('#user_name').val().length;
    if(len<5||len>20)
    {
        $('#user_name').next().html('Please enter username of 5~20 characters');
        $('#user_name').next().show();
        return false;
    }
    else
    {
        $('#user_name').next().hide();
        return true;
    }
}

function check_pwd(){
    var len = $('#pwd').val().length;
    if(len<8||len>20)
    {
        $('#pwd').next().html('Please enter password of 8 ~ 20 characters')
        $('#pwd').next().show();
        return false
    }
    else
    {
        $('#pwd').next().hide();
        return true;
    }
}