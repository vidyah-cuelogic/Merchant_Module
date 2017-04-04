$(document).ready(function() {
    $('#contact_form').bootstrapValidator({        
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            email: {                
                validators: {
                    notEmpty: {
                        message: 'Please provide email address'
                    },
                    identical:
                    {   field: 'email1',
                        message: 'email is not same as confirm email '
                    },
                    emailAddress: {
                        message: 'Please provide a valid email address'
                    }
                }
            },
            email1: {                
                validators: {
                    notEmpty: {
                        message: 'Please provide email address'
                    },
                    identical:
                    {   field: 'email',
                        message: 'confirm email is not same as email'
                    },
                    emailAddress: {
                        message: 'Please supply a valid email address'
                    }
                }
            },
            first_name: {               
                validators: {
                        stringLength: 
                    {                    
                        min: 2,                    
                        max: 100,                    
                        message:'first_name should have at least two character'                            
                    },
                        notEmpty: {
                        message: 'Please provide your first name with no space'
                    }
                }
            },
            last_name: {               
                validators: {
                    stringLength: 
                    {                    
                        min: 2,                    
                        max: 100,                    
                        message:'first_name should have at least two character'                            
                    },
                        
                        notEmpty: {
                        message: 'Please provide your last name with no space'
                    }
                }
            },
            password: {               
                validators: {
                    stringLength: 
                    {                    
                        min: 8,                    
                        max: 16,                    
                        message:'password must have at least 8 character and maximum 16 characters'                            
                    },
                    regexp:
                    {
                        regexp: /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-z\d]+$/, 

                        message: 'The password should contain at least 1 Uppercase Alphabet, 1 Lowercase Alphabet, 1 Number '
                    },
                    identical:
                    {   field:"password1",
                        message: 'password should be same as below '
                    },
                    notEmpty:
                     {
                        message: 'Please provide password'
                    }
                                   
                }
            },
            
            password1: {                
                validators: {
                    notEmpty: {
                        message: 'Please provide  password for confiramation'
                    },
                    identical:
                    {   field:"password",
                        message: 'password should be same as above '
                    }
                }
            },
            }
        })
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") 
                $('#contact_form').data('bootstrapValidator').resetForm();
           e.preventDefault();            
            var $form = $(e.target);            
            var bv = $form.data('bootstrapValidator');            
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});
