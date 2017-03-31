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
                        message: 'Email address is required'
                    },
                    
                    emailAddress: {
                        message: 'Please provide a valid email address'
                    }
                }

            },
            email1: {
                
                validators: {
                    notEmpty: {
                        message: 'Email address is required'
                    },
                    identical:
                    {   field: 'email',
                        message: 'Email should be same as above email'
                    },
                    
                }

            },
            terms: {
            validators: {
                notEmpty: {
                    message: 'You must agree with the terms and conditions'
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
                        message: 'First Name is required '
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
                        regexp: /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&])[a-zA-z\d!@#$%^&]+$/, 

                        message: 'Please provide valid password'
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

