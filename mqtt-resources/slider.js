var broker = 'wss://mqtt.eclipse.org:443/mqtt';
        var client  = mqtt.connect(broker);

        var status_header = document.getElementById('status-header')

        client.on('connect', function () {
            status_header.innerHTML = 'Connected to '+broker; 
            console.log('Connected to '+broker)
        })
        //payload to be passed
            let data = {
                temperature: 0,
                pressure: 1013,
                gyroX: 0,
                gyroY: 0,
                gyroZ: 0,
                accelerometerX:0,
                accelerometerY:0,
                accelerometerZ:0,
                magnetometerX:0,
                magnetometerY:0,
                magnetometerZ:0,
                humidity:0,
                proximity: 0,
                colorR: 0,
                colorG: 0,
                colorB: 0,
                colorC: 0,
            };
        //object defined functions
            let functions = {
                input: (e) => {
                    let name = e.target.name;
                    let value = $(`input[name=${name}]`).val();
                    $(`#${name}`).text(value);                
                },
                mouseup: (e) => {
                    let name = e.target.name;
                    let value = $(`input[name=${name}]`).val();
                    data[name] = value;
                    client.publish('clue-slider', JSON.stringify(data));
                }
            };

            let sliders = $(".slider");
            console.log(sliders);
            for(let slider of sliders) {
                for(let key in functions) {
                    slider.addEventListener(key, functions[key]);
                }
            }