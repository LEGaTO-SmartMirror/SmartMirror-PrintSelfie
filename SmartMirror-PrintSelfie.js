/**
 * @file smartmirror-MaryTTS.js
 *
 * @author nkucza
 * @license MIT
 *
 * @see  https://github.com/NKucza/smartmirror-MaryTTS
 */

Module.register('SmartMirror-PrintSelfie',{

	defaults: {

	},

	start: function() {
		this.sendSocketNotification('CONFIG', this.config);
		Log.info('Starting module: ' + this.name);
	},

	notificationReceived: function(notification, payload, sender) {
		if(notification === 'TAKE_SELFIE') {
			//this.sendSocketNotification('TTS-en', "f");
			this.sendSocketNotification('TAKE_SELFIE', payload);
		}
	},

	//say_message

  // Subclass socketNotificationReceived received.
  socketNotificationReceived: function(notification, payload) {
	if(notification === 'say_message') {
		self.sendNotification("SHOW_ALERT", {type: "notification", message: payload});
	}
  }

});
