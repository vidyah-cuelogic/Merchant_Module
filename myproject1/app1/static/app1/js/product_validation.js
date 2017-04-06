$(document).ready(function() {
    $('#myform').bootstrapValidator({
            feedbackIcons: {
            },
            fields: {
                product_name: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required '
                        }
                    }
                },
                category: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required'
                        }
                    }
                },
                product_specification: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required'
                        }
                    }
                },
                product_cost: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required'
                        }
                        
                    }
                },
                material_details: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required'
                        }
                    }
                },
                quantity: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required'
                        }
                    }
                },
                deliver_charges: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required'
                        }
                        
                    }
                },

            }
        })
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow")
            $('#myform').data('bootstrapValidator').resetForm();
            e.preventDefault();
            var $form = $(e.target);
            var bv = $form.data('bootstrapValidator');
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});




