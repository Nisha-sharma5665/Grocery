function registerUser()
{    
    if(ValidateForm())
    {   
    const password = $("input[name='password']").val();
    const passwordConfirm = $("input[name='passwordConfirm']").val();
        if (password === passwordConfirm) {
           $('#registerForm').submit();
        } else {
           alert("Password and Password confirm doesn't matched!");
        }
    }
    else{
        alert('Please fill all required fields!');
    }
}

function ValidateForm()
{
    var valid=true;
    $('.rquired').each((index,ement)=>{
        if($.trim($(ement).val())=='')
        {
            valid=false;
        }
    });
    return valid;
}
