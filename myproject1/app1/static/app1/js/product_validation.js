$(document).ready(function() {
    $('#myform').bootstrapValidator({
            feedbackIcons: {
            },
            fields: {
                product_name: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required '
                        },
                        stringLength: {
                            min: 2,
                            max: 150,
                            message: 'Product name should have at least two character maximum 150 character'
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
                product_details: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required'
                        },
                        stringLength: {
                            min: 2,
                            max: 500,
                            message: 'Product details should have at least two character maximum 1000 character'
                        }
                    }
                },
                product_cost: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required'
                        },
                        numeric: {
                            
                            decimalSeparator: '.',
                            message: 'The value is not a number'
                        }
                        
                    }
                },
                material_details: {
                    validators: {
                        notEmpty: {
                            message: 'Field is required'
                        },
                        stringLength: {
                            min: 2,
                            max: 1000,
                            message: 'Product name should have at least two character maximum 100 character'
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
                        },
                        numeric: {
                            
                            decimalSeparator: '.',
                            message: 'The value is not a number'
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




