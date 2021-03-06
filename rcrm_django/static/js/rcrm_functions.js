var TimeInt = 1000;
var TimeInt_for_Chat = TimeInt * 5;
var TimeInt_for_CRM = TimeInt * 2;


$(function()
    {
        $("#dialog_edit_client").dialog(
                {
                    autoOpen: false,
                    resizable: true,
                    height: "auto",
                    width: 500,
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

                                        jQuery.post('/clients/add_edit_client',{ 'sname':sname,
                                                                        'fname':fname,
                                                                        'inn':inn,
                                                                        'phone':phone,
                                                                        'priority':priority,
                                                                        'address':address,
                                                                        'mail':mail},
                                                                        function( data ) {
                                                                            if (data == "None")
                                                                                success_notify("Клиент создан/исправлен.");
                                                                            else
                                                                                error_notify(data);
                                                                        });

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
                    width: 450,
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
                                        is_new = $("#is_new").val();

                                        if (is_new == "yes"){
                                            jQuery.post('/users/add_user',{ 'login':login,
                                                                            'fname':fname,
                                                                            'lname':lname,
                                                                            'mail':mail,
                                                                            'pass':pass },
                                                                            function( data ) {
                                                                                if (data == "None")
                                                                                    success_notify("Пользователь создан.");
                                                                                else
                                                                                    error_notify(data);
                                                                            });
                                        }

                                        if (is_new == "no"){
                                            jQuery.post('/users/edit_user',{ 'login':login,
                                                                            'fname':fname,
                                                                            'lname':lname,
                                                                            'mail':mail,
                                                                            'pass':pass },
                                                                            function( data ) {
                                                                                if (data == "None")
                                                                                    success_notify("Пользователь изменён.");
                                                                                else
                                                                                    error_notify(data);
                                                                            });
                                        }

                                        setTimeout("show_users()",TimeInt);

                                        $("#is_new").val("yes");

                                        $(this).dialog("close");
                                    },
                            "Отмена": function()
                                    {
                                        $("#is_new").val("yes");

                                        $(this).dialog("close");
                                    }
                        }
                });
});


(function( $ ){
    //plugin buttonset vertical
    $.fn.buttonsetv = function() {
      $(':radio, :checkbox', this).wrap('<div style="margin: 1px"/>');
      $(this).buttonset();
      $('label:first', this).removeClass('ui-corner-left').addClass('ui-corner-top');
      $('label:last', this).removeClass('ui-corner-right').addClass('ui-corner-bottom');
      mw = 0; // max witdh
      $('label', this).each(function(index){
         w = $(this).width();
         if (w > mw) mw = w;
      })
      $('label', this).each(function(index){
        $(this).width(mw);
      })
    };
})( jQuery );


function error_notify(data)
    {
        Lobibox.notify( 'error', { size: 'mini', sound: false,  msg: "Запрос завершился с ошибкой: '"+data+"'.", delay: 10000 });
    }


function success_notify(message)
    {
        Lobibox.notify( 'success', { size: 'mini', sound: false,  msg: "Запрос выполнен успешно.", delay: 2000 });
    }


function show_crm(url)
    {
        var data = {"only_table":"true"};

        $.ajax({url: url,
            type: "POST",
            data: data,
            cache: false,
            success:function(html){
                $("#crm_content").html(html);
                $(function() {
                    $( "#dialog-link, #icons li" ).hover(
                        function() {
                            $( this ).addClass( "ui-state-hover" );
                        },
                        function() {
                            $( this ).removeClass( "ui-state-hover" );
                        }
                    );
                });
                $(function() {$( ".crm_radio_btns" ).buttonset();});
            }
        });
    }


function show_clients()
    {
        var data = {"only_table":"true"};

        $.ajax({url: "/clients/",
            type: "POST",
            data: data,
            cache: false,
            success:function(html){
                $("#clients_content").html(html);
                $(function() {$( ".cl_radio_btns" ).buttonset();});
            }
        });
    }


function show_users()
    {
        var data = {"only_table":"true"};

        $.ajax({url: "/users/",
            type: "POST",
            data: data,
            cache: false,
            success:function(html){
                $("#users_content").html(html);
                $(function() {$( ".cl_radio_btns" ).buttonset();});
            }
        });
    }


function get_chat()
    {
        $.ajax({url: "/chat/show_chat",
                cache: false,
                success:function(html){$("#chat_content").html(html);}});
    }


function rem_client(id)
    {
    	jQuery.post('/clients/rem_client',{'id':id},
    	                           function( data ) {
                                    if (data == "None")
                                        success_notify("Клиент удалён.");
                                    else
                                        error_notify(data);
                                  }
                   );
        setTimeout("show_clients()",TimeInt);
    }


function obj_switch_status( obj, id, status )
    {
        var url = "";
        var url_user = "/users/user_switch_status";
        var url_client = "/clients/client_switch_status";
        var url_task = "/crm/task_switch_status";

        if ( obj == "user" ) { url = url_user; }

        if ( obj == "client" ) { url = url_client; }

        if ( obj == "task" ) { url = url_task; }

    	jQuery.post( url , {'id':id, 'status':status},
    	                           function( data ) {
                                    if (data == "None")
                                        success_notify("Объект изменён.");
                                    else
                                        error_notify(data);
                                  }
                   );
    }


function show_add_edit_user_dialog(id)
    {
        if (id)
            {
                $('#add_edit_user_login').prop('disabled', true);
                $("#check_login_out").html("");
                $("#add_edit_user_pass").val("").html();
                $("#add_edit_user_login").val($("#user_"+id+"_login").html());
                $("#add_edit_user_fname").val($("#user_"+id+"_fname").html());
                $("#add_edit_user_lname").val($("#user_"+id+"_lname").html());
                $("#add_edit_user_mail").val($("#user_"+id+"_mail").html());
                $("#is_new").val("no");
            }

        if (!id)
            {
                $('#add_edit_user_login').prop('disabled', false);
                $("#check_login_out").html("");
                $("#add_edit_user_pass").val("").html();
                $("#add_edit_user_login").val("");
                $("#add_edit_user_fname").val("");
                $("#add_edit_user_lname").val("");
                $("#add_edit_user_mail").val("");
                $("#is_new").val("yes");
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
        if (!id) {
                $("#add_edit_client_sname").val("");
                $("#add_edit_client_fname").val("");
                $("#add_edit_client_inn").val("");
                $("#add_edit_client_address").val("");
                $("#add_edit_client_phone").val("");
                $("#add_edit_client_mail").val("");
                $("#add_edit_client_priority").val("");

                $("#add_edit_client_sname").prop('disabled', false);

                $("#dialog_edit_client").dialog("open");

                return;
        }

        var url = "/clients/get_client_info/" + id;

        jQuery.post(url,{'field':'sname'},function(data){$("#add_edit_client_sname").val(data);});
        jQuery.post(url,{'field':'name'},function(data){$("#add_edit_client_fname").val(data);});
        jQuery.post(url,{'field':'inn'},function(data){$("#add_edit_client_inn").val(data);});
        jQuery.post(url,{'field':'address'},function(data){$("#add_edit_client_address").val(data);});
        jQuery.post(url,{'field':'phone'},function(data){$("#add_edit_client_phone").val(data);});
        jQuery.post(url,{'field':'email'},function(data){$("#add_edit_client_mail").val(data);});
        jQuery.post(url,{'field':'priority'},function(data){$("#add_edit_client_priority").val(data);});

        $("#add_edit_client_sname").prop('disabled', true);

        $("#dialog_edit_client").dialog("open");
    }


function add_message()
    {
        jQuery.post('/chat/add_post', {message: $("#id_message").val()})
        get_chat();
        $("#id_message").val("");
    }


function set_cookie_hide_deleted_tasks(set)
    {
        jQuery.post('/crm/hide_closed_tasks',{ 'hide_closed_tasks':set });
        setTimeout("show_crm()",TimeInt);
    }


function set_cookie_my_tasks(set)
    {
        jQuery.post('/crm/only_my_tasks',{ 'only_my_tasks':set });
        setTimeout("show_crm()",TimeInt);
    }


function find_user()
    {
         var data = {find_user_name: $("#find_user_input_id").val()}

         if (data['find_user_name'] == ""){
            $("#find_user_render").html("");
            return;
         }

         $.ajax({
            url: "/users/find_user",
            type: "POST",
            data: data,
            success:function(html){
                    $("#find_user_render").html(html);
                    $(function() {$( ".cl_radio_btns" ).buttonset();});
            }
                 });
    }


function clear_find_by_inn()
    {
        $("#id_find_by_inn").val("");
        $("#crm_find_content").html("");
    }


function find_client()
    {
         var data = {find_client: $("#find_client_input_id").val()}

         if (data['find_client'] == ""){
            $("#find_client_render").html("");
            return;
         }

         $.ajax({
            url: "/clients/find_client",
            type: "POST",
            data: data,
            success:function(html){
                    $("#find_client_render").html(html);
                    $(function() {$( ".cl_radio_btns" ).buttonset();});
            }
                 });
    }


//Tasks namespace.
var Tasks = {

    add:    function(form_id)
	{
        jQuery.ajax({
             url: '/crm/add_task',
             type: "POST",
             dataType: "html",
             data: jQuery("#"+form_id).serialize(),
             success:   function( data ) {
                            if (data == "None")
                                success_notify("Заявка добавлена.");
                            else
                                error_notify(data);
                        }
        });

        $(':input',"#"+form_id)
            .not(':button, :submit, :reset, :hidden')
            .not('[name = priority]')
            .val('')
            .removeAttr('checked')
            .removeAttr('selected');
	},

	remove: function(id)
	{
	    jQuery.post('/crm/rem_task',{'id':id},
                                  function( data ) {
                                    if (data == "None")
                                        success_notify("Задание удалено.");
                                    else
                                        error_notify(data);
                                  }
                   );
	    setTimeout("show_crm()",TimeInt);
	},

	restore:    function(id)
	{},

	edit:   function(id)
	{},

	transfer_to:    function()
	{},

	sw_prio:    function()
	{},

	find_by_inn:    function()
    {
        var data = { 'inn': $("#id_find_by_inn").val() };

        if ( data['inn'] == "" )
            {
                $("#crm_find_content").html("");
                return;
            }

        $.ajax({
            url: "/crm/find_by_inn",
            type: "POST",
            data: data,
            success:
                function( html )
                    {
                        if ( html == "None" )
                            error_notify("Записей не найдено!");
                        else $("#crm_find_content").html(html);
                        $( ".crm_radio_btns" ).buttonset();
                    }
        });
    }

};
