'use strict';
const NodeHelper = require('node_helper');

const {PythonShell} = require('python-shell');
var pythonStarted = false;

module.exports = NodeHelper.create({

 /*	python_start: function () {
		const self = this;
    		self.pyshell = new PythonShell('modules/' + this.name + '/pythonscripts/stringToTTS.py', { pythonPath: 'python', args: [JSON.stringify(this.config)]});

    		self.pyshell.on('message', function (message) {
			try{
				var parsed_message = JSON.parse(message)
				//console.log("[MSG " + self.name + "] " + message);
      				if (parsed_message.hasOwnProperty('status')){
      					console.log("[" + self.name + "] " + parsed_message.status);
      				}
			}
			catch(err) {
				//console.log(err)
			}
    		});
			
  	}, */

  // Subclass socketNotificationReceived received.
  socketNotificationReceived: function(notification, payload) {
 		const self = this;
 	if(notification === 'TAKE_SELFIE') {
		self.pyshell = new PythonShell('modules/' + this.name + '/python_scripts/print_service.py', { pythonPath: 'python3', args: payload});
	
		self.pyshell.on('message', function (message) {
			try{
				var parsed_message = JSON.parse(message)
				//console.log("[MSG " + self.name + "] " + message);
      				if (parsed_message.hasOwnProperty('status')){
      					console.log("[" + self.name + "] " + parsed_message.status);
      				}else if (parsed_message.hasOwnProperty('say_message')){
					self.sendSocketNotification('say_message', parsed_message.say_message)
				}
			}
			catch(err) {
				//console.log(err)
			}
    		});
	
        };
  }
});
