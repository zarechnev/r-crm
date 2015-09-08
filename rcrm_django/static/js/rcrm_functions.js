var TimeInt = 20000;

function show_crm()
    {
        var data = {"only_table":"true"};

        $.ajax({url: "/crm/",
            type: "POST",
            data: data,
            cache: false,
            success:function(html){$("#crm_content").html(html);}});
    }

function show_clients()
    {
        var data = {"only_table":"true"};

        $.ajax({url: "/clients/",
            type: "POST",
            data: data,
            cache: false,
            success:function(html){$("#clients_content").html(html);}});
    }

function show_users()
    {
        var data = {"only_table":"true"};

        $.ajax({url: "/users/",
            type: "POST",
            data: data,
            cache: false,
            success:function(html){$("#users_content").html(html);}});
    }

function add_task()
	{
		inn = jQuery('#id_inn').val().split(' ')[0];
		comment = jQuery('#id_comment').val();
		if (inn != "")
			{
				if (comment != "")
					{
						jQuery("#id_inn").val('');
						jQuery("#id_comment").val('');
						jQuery.post('/crm/add_task',{'inn':inn, 'comment':comment},setTimeout("show_crm()",TimeInt));
					}
			}
	}

function get_chat()
    {
        $.ajax({url: "/chat/show_chat",
                cache: false,
                success:function(html){$("#chat_content").html(html);}});
    }

function rem_task(id)
	{
	    jQuery.post('/crm/rem_task',{'id':id},setTimeout("show_crm()",TimeInt));
	}

function rem_client(id)
    {
    	jQuery.post('/clients/rem_client',{'id':id},setTimeout("show_clients()",TimeInt));
    }

function rem_user(id)
    {
    	jQuery.post('/users/rem_user',{'id':id},setTimeout("show_users()",TimeInt));
    }

function show_add_edit_user_dialog(id)
    {
        if (id != "")
            {
                $("#add_edit_user_login").val($("#user_"+id+"_login").html());
                $("#add_edit_user_fname").val($("#user_"+id+"_fname").html());
                $("#add_edit_user_lname").val($("#user_"+id+"_lname").html());
                $("#add_edit_user_mail").val($("#user_"+id+"_mail").html());
            }

        $("#dialog_edit_users").dialog("open");
    }

function check_unique_login()
    {
        var data = {login: $("#add_edit_user_login").val()}

         $.ajax({
            url: "/users/check_login",
            type: "POST",
            data: data,
            success:function(html){$("#check_login_out").html(html);}});
    }

function show_add_edit_client_dialog(id)
    {
        var url = "/clients/get_client_info/" + id;

        $.getJSON(  url,
                    function(data) {
                        var obj = JSON.parse(data);
                        $("#add_edit_client_sname").html(obj.fields.sname);
                        $("#add_edit_client_fname").val(obj.fields.name).html();
                        $("#dialog_edit_client").dialog("open");
                    });

        var jqxhr = $.getJSON(url);


        var obj = $.parseJSON(jqxhr);

        jqxhr.complete(function() {alert(obj.fields.sname)});
    }

$(function()
    {
        $("#dialog_edit_client").dialog(
                {
                    autoOpen: false,
                    resizable: true,
                    height: "auto",
                    width: "auto",
                    modal: true,
                    buttons:
                        {
                            "Сохранить": function()
                                    {
                                        sname = $("#add_edit_client_sname").val();
                                        fname = $("#add_edit_client_fname").val();
                                        inn = $("#add_edit_client_inn").val();
                                        phone = $("#add_edit_client_phone").val();
                                        mail = $("#add_edit_client_mail").val();
                                        address = $("#add_edit_client_address").val();
                                        priority = $("#add_edit_client_priority").val();

                                        jQuery.post('/clients/add_client',{ 'sname':sname,
                                                                        'fname':fname,
                                                                        'inn':inn,
                                                                        'phone':phone,
                                                                        'priority':priority,
                                                                        'address':address,
                                                                        'mail':mail});

                                        setTimeout("show_clients()",TimeInt);

                                        $(this).dialog("close");
                                    },
                            "Отмена": function()
                                    {
                                        $(this).dialog("close");
                                    }
                        }
                });
    });


$(function()
    {
        $("#dialog_edit_users").dialog(
                {
                    autoOpen: false,
                    resizable: true,
                    height: "auto",
                    width: "auto",
                    modal: true,
                    buttons:
                        {
                            "Сохранить": function()
                                    {
                                        login = $("#add_edit_user_login").val();
                                        fname = $("#add_edit_user_fname").val();
                                        lname = $("#add_edit_user_lname").val();
                                        mail = $("#add_edit_user_mail").val();
                                        pass = $("#add_edit_user_pass").val();

                                        jQuery.post('/users/add_user',{ 'login':login,
                                                                        'fname':fname,
                                                                        'lname':lname,
                                                                        'mail':mail,
                                                                        'pass':pass});

                                        setTimeout("show_users()",TimeInt);

                                        $(this).dialog("close");
                                    },
                            "Отмена": function()
                                    {
                                        $(this).dialog("close");
                                    }
                        }
                });
});

function add_message()
    {
        jQuery.post('/chat/add_post', {message: $("#id_message").val()})
        get_chat();
        $("#id_message").val("");
    }