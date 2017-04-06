key=$('#color1').val();
            console.log("color key = "+key);
            color_mapping[key].push(e.target.result);

            color_mapping[template1] = []
            data['color_mapping'] = color_mapping